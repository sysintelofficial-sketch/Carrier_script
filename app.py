import streamlit as st

# Page Config
st.set_page_config(page_title="Dispatch Pro", layout="centered")

st.markdown("""
    <style>
    .script-box { background-color: #f0f2f6; padding: 20px; border-radius: 10px; font-size: 18px; border-left: 5px solid #0047AB; }
    </style>
""", unsafe_allow_html=True)

st.title("📞 Fast-Track Dispatcher Script")

# Step-by-Step UI
step = st.radio("Conversation Stage", ["1. Intro & Filter", "2. The Value Hook", "3. The Closing/Next Step"])

if step == "1. Intro & Filter":
    st.markdown("### Stage 1: The Opener (10 Seconds)")
    st.markdown("""
    <div class='script-box'>
    <b>[You]:</b> 'Good morning! This is Ahsan, I’m a professional dispatcher. I’ll keep this quick—are you running your own authority right now, or are you leased on?'
    </div>
    """, unsafe_allow_html=True)
    st.info("If they say 'Leased' -> 'No problem, have a good one!' (Hang up)")
    st.info("If they say 'My own authority' -> Proceed to Step 2.")

elif step == "2. The Value Hook":
    st.markdown("### Stage 2: The Value (20 Seconds)")
    st.markdown("""
    <div class='script-box'>
    <b>[You]:</b> 'Got it. I specialize in booking premium lanes for independent carriers. I’m not looking for a contract today—I just want to prove I can get you better rates than you're currently seeing on the boards. What kind of equipment are you running today?'
    </div>
    """, unsafe_allow_html=True)
    st.warning("Keep it brief. Let them talk about their truck/location.")

elif step == "3. The Closing/Next Step":
    st.markdown("### Stage 3: The Call to Action (15 Seconds)")
    st.markdown("""
    <div class='script-box'>
    <b>[You]:</b> 'That’s a good lane. Look, let’s do a two-load trial. No commitment. If I can't beat your current profit margin, we don't work together—simple as that. Does that sound fair?'
    
    <b>[If YES]:</b> 'Perfect. What’s your MC number so I can check your setup, and what’s the best email to send over the packet?'
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.caption("Pro Tip: If they sound busy, ask: 'Do you have 30 seconds for a quick pitch, or should I call you back at a better time?'")
