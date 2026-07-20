import streamlit as st
from gtts import gTTS
import io

# Page setup - "wide" layout to spread across the full screen
st.set_page_config(page_title="Dispatcher Pro", layout="wide")

st.markdown("""
    <style>
    /* Font size increase for better readability */
    .chat-box { 
        padding: 20px; 
        border-radius: 12px; 
        font-size: 22px !important; 
        line-height: 1.6;
        margin-bottom: 15px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
    }
    .you-box { background-color: #e3f2fd; color: #0d47a1; }
    .carrier-box { background-color: #ffebee; color: #b71c1c; }
    </style>
""", unsafe_allow_html=True)

st.title("📞 Professional Dispatcher Trainer")
st.subheader("Practice your flow with larger, clearer text")

dialogue = [
    {"role": "You", "text": "Hi [Name], this is Ahsan. Are you looking for extra freight support?"},
    {"role": "Carrier", "text": "Not really, we're doing okay. Why are you calling?"},
    {"role": "You", "text": "I understand. I work with private lanes that pay above average. Should I send my info?"},
    {"role": "Carrier", "text": "Sure, send it over, I'll take a look."},
    {"role": "You", "text": "Perfect, I'll email that now. I'll follow up in a few days. Thanks!"}
]

for line in dialogue:
    # Creating a wide layout with columns
    col1, col2 = st.columns([0.85, 0.15])
    
    with col1:
        box_class = "you-box" if line['role'] == "You" else "carrier-box"
        st.markdown(f"""
            <div class="chat-box {box_class}">
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
            st.write("")
