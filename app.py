import streamlit as st
from gtts import gTTS
import io

st.set_page_config(page_title="Dispatch Trainer", layout="centered")

# Dialogue Data
dialogue = [
    {"role": "You", "text": "Hi [Name], this is Ahsan. I'm a professional dispatcher—are you looking for extra freight support right now?"},
    {"role": "Carrier", "text": "Not really, we're doing okay on our own. Why are you calling?"},
    {"role": "You", "text": "I understand. I work with private lanes that pay above market average. If you ever need a hand, should I send you my info for your files?"},
    {"role": "Carrier", "text": "Sure, send it over, I'll take a look if we get stuck."},
    {"role": "You", "text": "Perfect, I'll email that right now. I'll follow up in a few days. Thanks for your time!"}
]

st.title("🎧 Dispatcher Audio Trainer")

for i, line in enumerate(dialogue):
    # Box styling based on role
    bg_color = "#dbeafe" if line['role'] == "You" else "#fee2e2"
    st.markdown(f"""
        <div style="background-color: {bg_color}; padding: 15px; border-radius: 10px; margin-bottom: 10px;">
            <strong style="color: #1e3a8a;">{line['role']}:</strong> {line['text']}
        </div>
    """, unsafe_allow_html=True)
    
    # Text-to-Speech Generation
    if line['role'] == "You":
        text_to_speak = line['text']
        tts = gTTS(text=text_to_speak, lang='en', slow=False)
        
        # Save to buffer
        audio_buffer = io.BytesIO()
        tts.write_to_fp(audio_buffer)
        audio_buffer.seek(0)
        
        # Audio Player
        st.audio(audio_buffer, format='audio/mp3')
    
    st.write("---")

st.sidebar.success("💡 Tip: Listen to the audio and repeat it exactly like that to improve your accent.")
