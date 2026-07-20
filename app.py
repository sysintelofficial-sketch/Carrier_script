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
    .emergency-box { background-color: #fff3e0; color: #e65100; border-left: 10px solid #ef6c00; }
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

# --- QUICK RESPONSES (Short & Punchy for live calls) ---
scenarios = {
    "I am driving / I am busy": {
        "reply": "I understand. Stay safe. I have well-paying private lanes. May I email my info as a backup?"
    },
    "What is this about?": {
        "reply": "I work with private lanes that pay above average. I want to be a backup for you. May I email my details?"
    },
    "We do not need help right now": {
        "reply": "No problem at all. I just want to be an option in your back pocket. May I email my info?"
    },
    "We have our own brokers": {
        "reply": "That is great. I am just reaching out to be an alternative option. May I send a quick email?"
    },
    "Who are you?": {
        "reply": "I am Ahsan, an independent logistics partner. I have specific lanes that pay well. May I email you my details?"
    },
    "Just send me an email": {
        "reply": "Perfect. I will send it right now. Thank you for your time."
    },
    "How did you get my number?": {
        "reply": "From the public FMCSA registry. You have a strong safety record, so I reached out."
    },
    "What kind of freight do you have?": {
        "reply": "Mostly dry van and reefer on regional routes. May I email you our active list?"
    },
    "We are covered for the week": {
        "reply": "Excellent. I will just email my contact details so you have a backup for next week."
    },
    "What are your rates like?": {
        "reply": "We pay above market average to keep good trucks moving. May I email you some examples?"
    }
}

# --- DEEP ENGAGEMENT (Short but impactful) ---
deep_engagement_scenarios = {
    "Why work with you instead of a big broker?": {
        "reply": "Big brokers keep large margins. I operate independently, so my margins are low, and more money goes to your truck."
    },
    "How do you pay your carriers?": {
        "reply": "Standard pay is thirty days, but we offer quick pay too. Cash flow is important. I will email the details."
    },
    "How does your onboarding work?": {
        "reply": "Very simple. I send a secure link, you upload your documents, and we are ready to go."
    }
}

# 1. Opening Line
st.subheader("Start with this:")
st.markdown('<div class="chat-box you-box"><b>You:</b> Hi, this is Ahsan. I am reaching out to see if you have any open trucks looking for loads today?</div>', unsafe_allow_html=True)

# 2. Dropdown for Quick Carrier Responses
st.markdown("---")
st.subheader("⚡ Quick Responses (Busy or Short Answers)")
choice = st.selectbox("Select the common scenario:", [""] + list(scenarios.keys()))

if choice:
    response_text = scenarios[choice]["reply"]
    st.markdown(f'<div class="chat-box carrier-box"><b>Carrier says:</b> {choice}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="chat-box you-box"><b>Your Reply:</b> {response_text}</div>', unsafe_allow_html=True)
    
    if st.button(f"Listen to your response for: {choice}"):
        with st.spinner("Generating audio..."):
            audio_bytes = asyncio.run(generate_male_audio(response_text))
            st.audio(audio_bytes, format='audio/mp3')

# 3. Dropdown for Deep Engagement
st.markdown("---")
st.subheader("🤝 Deep Engagement (Detailed questions)")
deep_choice = st.selectbox("Select the detailed question:", [""] + list(deep_engagement_scenarios.keys()))

if deep_choice:
    deep_response_text = deep_engagement_scenarios[deep_choice]["reply"]
    st.markdown(f'<div class="chat-box carrier-box"><b>Carrier asks:</b> {deep_choice}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="chat-box you-box"><b>Your Reply:</b> {deep_response_text}</div>', unsafe_allow_html=True)
    
    if st.button(f"Listen to your response for: {deep_choice}", key="deep_btn"):
        with st.spinner("Generating audio..."):
            audio_bytes = asyncio.run(generate_male_audio(deep_response_text))
            st.audio(audio_bytes, format='audio/mp3')

# 4. EMERGENCY ROUTE (If you don't know the answer)
st.markdown("---")
st.subheader("🚨 Emergency (If they ask something you don't know)")
emergency_text = "Good question. Let me check my system. I will put the exact details in the email I am sending you right now."
st.markdown(f'<div class="chat-box emergency-box"><b>Your Escape Reply:</b> {emergency_text}</div>', unsafe_allow_html=True)

if st.button("Listen to Emergency Response"):
    with st.spinner("Generating audio..."):
        audio_bytes = asyncio.run(generate_male_audio(emergency_text))
        st.audio(audio_bytes, format='audio/mp3')
