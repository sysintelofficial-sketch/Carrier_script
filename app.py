import streamlit as st
import asyncio
import edge_tts

# 1. Page Setup
st.set_page_config(page_title="Carrier Pitch Trainer", layout="wide")

# 2. Custom CSS
st.markdown("""
    <style>
    .chat-box { padding: 20px; border-radius: 12px; font-size: 22px !important; line-height: 1.6; margin-bottom: 15px; box-shadow: 2px 2px 8px rgba(0,0,0,0.1); }
    .you-box { background-color: #e3f2fd; color: #0d47a1; border-left: 8px solid #1976d2; }
    .carrier-box { background-color: #ffebee; color: #b71c1c; border-left: 8px solid #d32f2f; }
    </style>
""", unsafe_allow_html=True)

st.title("📞 Updated Professional Cold Call Script")

async def generate_male_audio(text):
    communicate = edge_tts.Communicate(text, "en-US-GuyNeural")
    audio_data = bytearray()
    async for chunk in communicate.stream():
        if chunk["type"] == "audio":
            audio_data.extend(chunk["data"])
    return bytes(audio_data)

# Updated Dialogue Script
dialogue = [
    {"role": "You", "text": "Hi, this is Ahsan. I’m reaching out to see if you have any open trucks that need freight support today?"},
    {"role": "Carrier", "text": "We're actually pretty busy right now, but thanks for the call."},
    {"role": "You", "text": "I completely understand! I work with private lanes in your area that pay above average. Should I send my info so you have me as a backup for when things slow down?"},
    {"role": "Carrier", "text": "Sure, send it over, I'll take a look."},
    {"role": "You", "text": "Perfect, I'll email that right now. Have a great day and stay safe out there!"}
]

# Display Loop
for line in dialogue:
    col1, col2 = st.columns([0.85, 0.15])
    with col1:
        box_class = "you-box" if line['role'] == "You" else "carrier-box"
        st.markdown(f'<div class="chat-box {box_class}"><b>{line["role"]}:</b> {line["text"]}</div>', unsafe_allow_html=True)
    
    with col2:
        if line['role'] == "You":
            audio_bytes = asyncio.run(generate_male_audio(line['text']))
            st.write("<br>", unsafe_allow_html=True) 
            st.audio(audio_bytes, format='audio/mp3')
