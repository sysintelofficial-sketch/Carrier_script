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
    },
    # --- 4 NEW COMMON SCENARIOS ---
    "How did you get my number?": {
        "reply": "I found your information on the public FMCSA registry. I noticed your safety record is strong, and I am looking for reliable carriers to partner with on future freight."
    },
    "What kind of freight do you have?": {
        "reply": "We focus on dry van and reefer loads, mostly regional and over-the-road routes. I can send a list of our active lanes to your email if you are interested."
    },
    "We are covered for the week": {
        "reply": "That is excellent. I do not want to interrupt your current schedule. I will just send a short email with my contact details so you have a reliable backup for next week."
    },
    "What are your rates like?": {
        "reply": "Our rates depend on the specific lane and market conditions, but we always aim to pay above the market average to keep good carriers moving. May I email you some recent examples?"
    }
}

# --- NEW DEEP ENGAGEMENT SCENARIOS ---
deep_engagement_scenarios = {
    "Why should I work with you instead of a big broker?": {
        "reply": "Because I offer direct communication and full transparency. When you call, you speak directly with me. I focus on building long-term partnerships rather than just covering a single load."
    },
    "How do you pay your carriers?": {
        "reply": "We process payments quickly because we know cash flow is important for your trucks. Standard pay is thirty days, but we also offer quick pay options. I will send the full payment details to your email."
    },
    "How does your onboarding process work?": {
        "reply": "It is very simple. I will send you an email with a secure link. You just upload your insurance and authority documents. Once approved, we can start moving freight together immediately."
    }
}

# 1. Opening Line
st.subheader("Start with this:")
st.markdown('<div class="chat-box you-box"><b>You:</b> Hi, this is Ahsan. I am reaching out to see if you have any open trucks that need freight support today?</div>', unsafe_allow_html=True)

# 2. Dropdown for Quick Carrier Responses
st.markdown("---")
st.subheader("⚡ Quick Responses (Busy or Short Answers)")
choice = st.selectbox("Select the common scenario:", [""] + list(scenarios.keys()))

# Dynamic Response for Quick Scenarios
if choice:
    response_text = scenarios[choice]["reply"]
    st.markdown(f'<div class="chat-box carrier-box"><b>Carrier says:</b> {choice}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="chat-box you-box"><b>Your Reply:</b> {response_text}</div>', unsafe_allow_html=True)
    
    if st.button(f"Listen to your response for: {choice}"):
        with st.spinner("Generating audio..."):
            audio_bytes = asyncio.run(generate_male_audio(response_text))
            st.audio(audio_bytes, format='audio/mp3')

# 3. Dropdown for Deep Engagement (When Carrier wants to talk)
st.markdown("---")
st.subheader("🤝 Deep Engagement (Carrier wants more details)")
st.info("Use these answers when the carrier has time and is asking detailed questions to build trust.")
deep_choice = st.selectbox("Select the detailed question:", [""] + list(deep_engagement_scenarios.keys()))

# Dynamic Response for Deep Engagement
if deep_choice:
    deep_response_text = deep_engagement_scenarios[deep_choice]["reply"]
    st.markdown(f'<div class="chat-box carrier-box"><b>Carrier asks:</b> {deep_choice}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="chat-box you-box"><b>Your Reply:</b> {deep_response_text}</div>', unsafe_allow_html=True)
    
    if st.button(f"Listen to your response for: {deep_choice}", key="deep_btn"):
        with st.spinner("Generating audio..."):
            audio_bytes = asyncio.run(generate_male_audio(deep_response_text))
            st.audio(audio_bytes, format='audio/mp3')
