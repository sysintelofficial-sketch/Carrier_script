import streamlit as st
from gtts import gTTS
import io

# Page setup for a wide look (پوری سکرین پر پھیلانے کے لیے)
st.set_page_config(page_title="Dispatcher Pro", layout="wide")

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
    # Create columns: 85% for text, 15% for audio player (Wide سکرین کے حساب سے سیٹ کیا گیا ہے)
    col1, col2 = st.columns([0.85, 0.15])
    
    with col1:
        color = "#e1f5fe" if line['role'] == "You" else "#ffebee"
        # Font size 22px اور باکس کو تھوڑا بڑا کر دیا گیا ہے
        st.markdown(f"""
            <div style="background-color: {color}; padding: 20px; border-radius: 12px; font-size: 22px; line-height: 1.6; box-shadow: 2px 2px 5px rgba(0,0,0,0.05);">
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
            
            # آڈیو بٹن کو بڑے ٹیکسٹ باکس کے بالکل سامنے لانے کے لیے تھوڑی سی سپیس
            st.write("<br>", unsafe_allow_html=True)
            st.audio(audio_buffer, format='audio/mp3')
        else:
            st.write("") # Empty space for Carrier side

    st.write("") # Small gap between lines
