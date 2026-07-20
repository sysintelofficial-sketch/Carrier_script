import streamlit as st
import asyncio
import edge_tts

# 1. Page Setup
st.set_page_config(page_title="Smart Carrier Pitch Trainer", layout="wide")

# 2. Custom CSS
st.markdown("""
    <style>
    .chat-box { padding: 20px; border-radius: 12px; font-size: 20px !important; line-height: 1.6; margin-bottom: 15px; }
    .you-box { background-color: #e3f2fd; color: #0d47a1; border-left: 8px solid #1976d2; }
    .carrier-box { background-color: #ffebee; color: #b71c1c; border-left: 8px solid #d32f2f; }
    .highlight { font-weight: bold; color: #2e7d32; }
    </style>
""", unsafe_allow_html=True)

st.title("📞 Smart Carrier Pitch: The Email Pivot Trainer")

# Async function for Audio
async def generate_male_audio(text):
    communicate = edge_tts.Communicate(text, "en-US-GuyNeural")
    audio_data = bytearray()
    async for chunk in communicate.stream():
        if chunk["type"] == "audio":
            audio_data.extend(chunk["data"])
    return bytes(audio_data)

# --- THE SMART SCENARIOS ---
scenarios = {
    "I'm driving / I'm busy": {
        "reply": "I totally understand, stay safe. I'll be quick—I have some private lanes with great rates. Mind if I email you my info as a backup for when things open up?"
    },
    "What is this about?": {
        "reply": "I work with private lanes that pay above-average. I'm just looking to be a reliable backup option for you. Can I send my details to your email?"
    },
    "We don't need help right now": {
        "reply": "No worries, I get it. I'm not looking to change your setup today, just want to be an option in your back pocket. Can I send an email so you have my info?"
    },
    "We have our own brokers": {
        "reply": "That's great, I'm glad you have good partners. I'm just reaching out to be an alternative if they ever drop the ball. Mind if I send you a quick email?"
    },
    "Who are you / Where are you from?": {
        "reply": "I'm Ahsan, an independent logistics partner. I work with specific lanes that pay well. I'd love to email you my details so you can see if we're a match."
    },
    "Just send me an email": {
        "reply": "Perfect, I'll get that over right now. Appreciate your time, stay safe out there!"
    }
}

# 1. Opening Line
st.subheader("Start with this:")
st.markdown('<div class="chat-box you-box"><b>You:</b> Hi, this is Ahsan. I’m reaching out to see if you have any open trucks that need freight support today?</div>', unsafe_allow_html=True)

# 2. Dropdown for Carrier Response
st.subheader("Select what the Carrier says:")
choice = st.selectbox("Choose the objection:", list(scenarios.keys()))

# 3. Dynamic Response based on choice
if choice:
    response_text = scenarios[choice]["reply"]
    
    st.markdown("---")
    st.markdown(f'<div class="chat-box carrier-box"><b>Carrier:</b> {choice}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="chat-box you-box"><b>Your Pivot to Email:</b> {response_text}</div>', unsafe_allow_html=True)
    
    if st.button("Listen to your response"):
        with st.spinner("Generating audio..."):
            audio_bytes = asyncio.run(generate_male_audio(response_text))
            st.audio(audio_bytes, format='audio/mp3')
