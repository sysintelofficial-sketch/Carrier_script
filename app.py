import streamlit as st
import asyncio
import edge_tts

# Page Setup
st.set_page_config(page_title="Smart Carrier Trainer", layout="wide")

# CSS for large, clear fonts and easy-to-read boxes
st.markdown("""
    <style>
    .chat-box { padding: 25px; border-radius: 15px; font-size: 24px !important; line-height: 1.8; margin-bottom: 20px; }
    .you-box { background-color: #e3f2fd; color: #0d47a1; border-left: 10px solid #1976d2; }
    .carrier-box { background-color: #ffebee; color: #b71c1c; border-left: 10px solid #d32f2f; }
    </style>
""", unsafe_allow_html=True)

st.title("📞 Smooth & Professional Carrier Pitch Trainer")

async def generate_male_audio(text):
    communicate = edge_tts.Communicate(text, "en-US-GuyNeural")
    audio_data = bytearray()
    async for chunk in communicate.stream():
        if chunk["type"] == "audio":
            audio_data.extend(chunk["data"])
    return bytes(audio_data)

# --- REVISED SCENARIOS (No Short Words, Clear Flow) ---
scenarios = {
    "I am driving / I am busy": {
        "reply": "I totally understand. Please stay safe. I will be very quick. I work with private lanes that pay above average. May I send my information to your email so you have it as a backup for later?"
    },
    "What is this about?": {
        "reply": "I work with private lanes that pay above average. I am just reaching out to be a reliable backup option for you. May I send my details to your email?"
    },
    "We do not need help right now": {
        "reply": "No problem at all, I completely understand. I just want to be an option in your back pocket. May I send you an email so you have my information for a future need?"
    },
    "We have our own brokers": {
        "reply": "That is great to hear. I am just reaching out to be an alternative if they ever do not have a load for you. May I send you a quick email?"
    },
    "Who are you?": {
        "reply": "I am Ahsan, an independent logistics partner. I work with specific lanes that pay well. I would like to email my details to you so you can see if we are a good match."
    },
    "Just send me an email": {
        "reply": "That is perfect. I will send that right now. Thank you for your time and stay safe out there."
    }
}

# 1. Opening Line
st.subheader("Start with this:")
st.markdown('<div class="chat-box you-box"><b>You:</b> Hi, this is Ahsan. I am reaching out to see if you have any open trucks that need freight support today?</div>', unsafe_allow_html=True)

# 2. Dropdown for Carrier Response
st.subheader("Select what the Carrier says:")
choice = st.selectbox("Select the scenario:", list(scenarios.keys()))

# 3. Dynamic Response
if choice:
    response_text = scenarios[choice]["reply"]
    st.markdown("---")
    st.markdown(f'<div class="chat-box carrier-box"><b>Carrier says:</b> {choice}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="chat-box you-box"><b>Your Reply:</b> {response_text}</div>', unsafe_allow_html=True)
    
    if st.button("Listen to your response"):
        with st.spinner("Generating audio..."):
            audio_bytes = asyncio.run(generate_male_audio(response_text))
            st.audio(audio_bytes, format='audio/mp3')
