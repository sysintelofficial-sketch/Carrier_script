import streamlit as st
from gtts import gTTS
import io

# Page setup for a compact look
st.set_page_config(page_title="Dispatcher Pro", layout="centered")

st.title("📞 Dispatcher Trainer")
st.write("Click the player button to listen to the line, then practice!")

dialogue = [
    {"role": "You", "text": "Hi [Name], this is Ahsan. Are you looking for extra freight support?"},
    {"role": "Carrier", "text": "Not really, we're doing okay. Why are you calling?"},
    {"role": "You", "text": "I understand. I work with private lanes that pay above average. Should I send my info?"},
    {"role": "Carrier", "text": "Sure, send it over, I'll take a look."},
    {"role": "You", "text": "Perfect, I'll email that now. I'll follow up in a few days. Thanks!"}
]

for i, line in enumerate(dialogue):
    # Create columns: 80% for text, 20% for audio player
    col1, col2 = st.columns([0.8, 0.2])
    
    with col1:
        color = "#e1f5fe" if line['role'] == "You" else "#ffebee"
        st.markdown(f"""
            <div style="background-color: {color}; padding: 10px; border-radius: 8px; font-size: 14px;">
                <b>{line['role']}:</b> {line['text']}
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        if line['role'] == "You":
            # Generate Audio
            tts = gTTS(text=line['text'], lang='en', slow=False)
            audio_buffer = io.BytesIO()
            tts.write_to_fp(audio_buffer)
            audio_buffer.seek(0)
            st.audio(audio_buffer, format='audio/mp3')
        else:
            st.write("") # Empty space for Carrier side

    st.write("") # Small gap between lines
