import streamlit as st
import asyncio
import edge_tts

# 1. Page Setup
st.set_page_config(page_title="Smart Carrier Trainer", layout="wide")

# 2. Custom CSS
st.markdown("""
    <style>
    .chat-box { padding: 20px; border-radius: 12px; font-size: 22px !important; line-height: 1.6; margin-bottom: 15px; box-shadow: 2px 2px 8px rgba(0,0,0,0.1); }
    .you-box { background-color: #e3f2fd; color: #0d47a1; border-left: 8px solid #1976d2; }
    .carrier-box { background-color: #ffebee; color: #b71c1c; border-left: 8px solid #d32f2f; }
    </style>
""", unsafe_allow_html=True)

st.title("📞 Smart Carrier Pitch Trainer")

# Async function for Audio
async def generate_male_audio(text):
    communicate = edge_tts.Communicate(text, "en-US-GuyNeural")
    audio_data = bytearray()
    async for chunk in communicate.stream():
        if chunk["type"] == "audio":
            audio_data.extend(chunk["data"])
    return bytes(audio_data)

# --- THE LOGIC ---
# Define the scenarios
scenarios = {
    "I'm busy / driving right now": {
        "reply": "I completely understand. I’ll keep it brief—I work with private lanes in your area that pay above average. Can I just email my info so you have me as a backup for when you're free?"
    },
    "What is this about?": {
        "reply": "I work with private lanes that pay above average. I'm just reaching out to see if I can be a backup contact for you when your usual lanes are slow. Should I send my info over?"
    },
    "We don't need help right now": {
        "reply": "No problem at all, I totally get it. I'm just trying to build my contact list for the future. May I send you a quick email so you have my info for a rainy day?"
    },
    "Just send me an email": {
        "reply": "Perfect, I'll send that right now! Have a great day and stay safe out there!"
    }
}

# 1. Opening Line
st.markdown('<div class="chat-box you-box"><b>You:</b> Hi, this is Ahsan. I’m reaching out to see if you have any open trucks that need freight support today?</div>', unsafe_allow_html=True)

# 2. Dropdown for Carrier Response
choice = st.selectbox("Select how the Carrier responds:", list(scenarios.keys()))

# 3. Dynamic Response based on choice
if choice:
    response_text = scenarios[choice]["reply"]
    
    # Display Carrier's simulated choice
    st.markdown(f'<div class="chat-box carrier-box"><b>Carrier:</b> {choice}</div>', unsafe_allow_html=True)
    
    # Display your response
    st.markdown(f'<div class="chat-box you-box"><b>Your Reply:</b> {response_text}</div>', unsafe_allow_html=True)
    
    # Generate and Play Audio
    if st.button("Listen to your reply"):
        with st.spinner("Generating audio..."):
            audio_bytes = asyncio.run(generate_male_audio(response_text))
            st.audio(audio_bytes, format='audio/mp3')
