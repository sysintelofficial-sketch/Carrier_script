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
    .closing-box { background-color: #e8f5e9; color: #1b5e20; border-left: 10px solid #2e7d32; }
    .voicemail-box { background-color: #f3e5f5; color: #4a148c; border-left: 10px solid #7b1fa2; }
    .interrupt-box { background-color: #e0f7fa; color: #006064; border-left: 10px solid #00acc1; }
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

# --- QUICK RESPONSES (Short & Punchy) ---
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

# --- DEEP ENGAGEMENT (Handling Hard Questions) ---
deep_engagement_scenarios = {
    "How do you increase profit?": {
        "reply": "I optimize lane routing to reduce empty miles. It is hard to explain the math on the phone, so I have sent the data in an email. Please check it and let me know if it works for you."
    },
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
st.subheader("1️⃣ Start with this:")
st.markdown('<div class="chat-box you-box"><b>You:</b> Hi, this is Ahsan. I am reaching out to see if you have any open trucks looking for loads today?</div>', unsafe_allow_html=True)

# 2. VOICEMAIL (If they don't pick up)
st.markdown("---")
st.subheader("2️⃣ 📩 If call goes to Voicemail / Auto-Attendant")
voicemail_text = "Hi, this is Ahsan. I am reaching out with some profitable lanes for your trucks. I know you are busy, so I am sending over my details via email. Please check your inbox. Let's connect soon."
st.markdown(f'<div class="chat-box voicemail-box"><b>Leave this message:</b><br>{voicemail_text}</div>', unsafe_allow_html=True)

if st.button("Listen to Voicemail Script"):
    with st.spinner("Generating audio..."):
        audio_bytes = asyncio.run(generate_male_audio(voicemail_text))
        st.audio(audio_bytes, format='audio/mp3')

# 3. Quick Responses
st.markdown("---")
st.subheader("3️⃣ ⚡ Quick Responses (Busy or Short Answers)")
choice = st.selectbox("Select the common scenario:", [""] + list(scenarios.keys()))

if choice:
    response_text = scenarios[choice]["reply"]
    st.markdown(f'<div class="chat-box carrier-box"><b>Carrier says:</b> {choice}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="chat-box you-box"><b>Your Reply:</b> {response_text}</div>', unsafe_allow_html=True)
    
    if st.button(f"Listen to your response for: {choice}"):
        with st.spinner("Generating audio..."):
            audio_bytes = asyncio.run(generate_male_audio(response_text))
            st.audio(audio_bytes, format='audio/mp3')

# 4. Deep Engagement
st.markdown("---")
st.subheader("4️⃣ 🤝 Deep Engagement (Detailed questions)")
deep_choice = st.selectbox("Select the detailed question:", [""] + list(deep_engagement_scenarios.keys()))

if deep_choice:
    deep_response_text = deep_engagement_scenarios[deep_choice]["reply"]
    st.markdown(f'<div class="chat-box carrier-box"><b>Carrier asks:</b> {deep_choice}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="chat-box you-box"><b>Your Reply:</b> {deep_response_text}</div>', unsafe_allow_html=True)
    
    if st.button(f"Listen to your response for: {deep_choice}", key="deep_btn"):
        with st.spinner("Generating audio..."):
            audio_bytes = asyncio.run(generate_male_audio(deep_response_text))
            st.audio(audio_bytes, format='audio/mp3')

# 5. NEW: POLITE INTERRUPTION (For Long Talkers)
st.markdown("---")
st.subheader("5️⃣ ✋ Polite Interruption (If they talk too much about tech/math)")
interrupt_text = "I would love to walk you through the analytics, but I know you have trucks to run and I do not want to hold you up. Let me email you the numbers and lanes. Once you see the data, we can jump on a quick call to discuss the details."
st.markdown(f'<div class="chat-box interrupt-box"><b>Your Reply to cut it short:</b><br>{interrupt_text}</div>', unsafe_allow_html=True)

if st.button("Listen to Polite Interruption"):
    with st.spinner("Generating audio..."):
        audio_bytes = asyncio.run(generate_male_audio(interrupt_text))
        st.audio(audio_bytes, format='audio/mp3')

# 6. EMERGENCY ROUTE 
st.markdown("---")
st.subheader("6️⃣ 🚨 Emergency (If they ask a question you don't know)")
emergency_text = "Good question. Let me check my system. I will put the exact details in the email I am sending you right now."
st.markdown(f'<div class="chat-box emergency-box"><b>Your Escape Reply:</b> {emergency_text}</div>', unsafe_allow_html=True)

# 7. HOW TO END THE CALL
st.markdown("---")
st.subheader("7️⃣ ✅ How to End the Call (Confirming their Email)")
closing_text = "I have your email as [Read Their Email], is that correct? ... Perfect. I am sending the details right now. Thank you for your time, stay safe!"
st.markdown(f'<div class="chat-box closing-box"><b>Your Final Words before hanging up:</b><br>{closing_text}</div>', unsafe_allow_html=True)

if st.button("Listen to Call Ending"):
    with st.spinner("Generating audio..."):
        tts_text = "I have your email as John at gmail dot com, is that correct? Perfect. I am sending the details right now. Thank you for your time, stay safe!"
        audio_bytes = asyncio.run(generate_male_audio(tts_text))
        st.audio(audio_bytes, format='audio/mp3')
