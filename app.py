import streamlit as st

# Page configuration
st.set_page_config(page_title="Professional Dispatcher", layout="centered")

# Styling for a clean, beautiful look
st.markdown("""
    <style>
    .chat-container { background-color: #f8fafc; padding: 20px; border-radius: 15px; border: 1px solid #e2e8f0; }
    .you { color: #1e40af; font-size: 18px; font-weight: bold; margin-bottom: 10px; padding: 10px; background: #dbeafe; border-radius: 8px; }
    .carrier { color: #991b1b; font-size: 18px; font-weight: bold; margin-bottom: 10px; padding: 10px; background: #fee2e2; border-radius: 8px; }
    </style>
""", unsafe_allow_html=True)

st.title("🚛 Dispatcher Professional Suite")
st.subheader("Your Conversation Flow")

# The Dialogue
with st.container():
    st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
    
    st.markdown("<div class='you'>[You]: Hi [Name], this is Ahsan. I'm a professional dispatcher—are you looking for extra freight support right now?</div>", unsafe_allow_html=True)
    
    st.markdown("<div class='carrier'>[Carrier]: Not really, we're doing okay on our own. Why are you calling?</div>", unsafe_allow_html=True)
    
    st.markdown("<div class='you'>[You]: I understand. I work with private lanes that pay above market average. If you ever need a hand, I'd love to help. Should I send you my info for your files?</div>", unsafe_allow_html=True)
    
    st.markdown("<div class='carrier'>[Carrier]: Sure, send it over, I'll take a look if we get stuck.</div>", unsafe_allow_html=True)
    
    st.markdown("<div class='you'>[You]: Perfect, I'll email that right now. I'll follow up in a few days. Thanks for your time!</div>", unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")

# Listening Practice Feature
st.subheader("🎤 Practice Your Speech")
st.write("Click the button below to record your voice and practice your script.")

# Using audio_input for real-time speech practice
audio_value = st.audio_input("Record your practice pitch")

if audio_value:
    st.audio(audio_value)
    st.success("Great! Listen to your recording to improve your tone and pace.")
