import streamlit as st

# Page Layout Configuration
st.set_page_config(page_title="Carrier Calling Script", page_icon="📞", layout="centered")

st.title("📞 Carrier Acquisition Script Matrix")
st.write("Select a talking mode based on the carrier's mood and situation. All scripts use simple, direct English.")

st.markdown("---")

# Sidebar navigation for 4 different modes
st.sidebar.header("🎛️ Choose Calling Mode")
calling_mode = st.sidebar.radio(
    "Select Tone:",
    [
        "Mode 1: Friendly & Casual (Relaxed)",
        "Mode 2: Fast & Urgent (Direct)",
        "Mode 3: Professional (Corporate)",
        "Mode 4: Problem Solver (Market Stress)"
    ]
)

# -------------------------------------------------------------------------
# MODE 1: FRIENDLY & CASUAL
# -------------------------------------------------------------------------
if "Mode 1" in calling_mode:
    st.subheader("😊 Mode 1: Friendly & Casual Tone")
    st.info("Best for: Friendly owner-operators who like a relaxed conversation.")
    
    st.markdown("### 📞 Dialogue Flow:")
    st.code('''
[You]: "Hey there! My name is Ahsan. I will keep this super short. Are you running under your own authority right now?"

[Carrier]: "Yes, I have my own authority."

[You]: "Awesome! Look, I know you are busy on the road, but we are looking for reliable carriers in your area right now. Are you open to looking at some high-paying loads for next week, or is your current setup keeping you completely busy?"
    ''', language="text")

# -------------------------------------------------------------------------
# MODE 2: FAST & URGENT
# -------------------------------------------------------------------------
elif "Mode 2" in calling_mode:
    st.subheader("⚡ Mode 2: Fast & Urgent Tone")
    st.info("Best for: Carriers who are in a hurry, driving, or want straight-to-the-point talk.")
    
    st.markdown("### 📞 Dialogue Flow:")
    st.code('''
[You]: "Hi, this is Ahsan. I will get straight to the point. We have a high-paying lane open right now and need an independent carrier immediately. Are your trucks loaded right now, or are you looking for a premium run?"

[Carrier]: "I am looking for a load. What do you have?"

[You]: "Perfect. We track capacity shortages to grab contract loads before they hit public boards. What kind of equipment do you have empty, and where do you want to go?"
    ''', language="text")

# -------------------------------------------------------------------------
# MODE 3: PROFESSIONAL
# -------------------------------------------------------------------------
elif "Mode 3" in calling_mode:
    st.subheader("👔 Mode 3: Professional & Structured Tone")
    st.info("Best for: Small fleet owners or well-established trucking companies.")
    
    st.markdown("### 📞 Dialogue Flow:")
    st.code('''
[You]: "Hello, my name is Ahsan. I am calling to see if your company is currently open to new dispatch partnerships to increase your fleet utility."

[Carrier]: "What exactly do you do?"

[You]: "We manage full back-office logistics, handle broker negotiations, and secure high-yield contract rates. Are you currently handling your own load bookings, or do you use a dedicated team to keep your trucks moving?"
    ''', language="text")

# -------------------------------------------------------------------------
# MODE 4: PROBLEM SOLVER
# -------------------------------------------------------------------------
elif "Mode 4" in calling_mode:
    st.subheader("🛠️ Mode 4: The Problem Solver Tone")
    st.info("Best for: Carriers complaining about low market rates and bad public load boards.")
    
    st.markdown("### 📞 Dialogue Flow:")
    st.code('''
[You]: "Hi, this is Ahsan. Look, I know the market is really tough right now and standard load boards are paying garbage rates. That is exactly why I am calling. We help owner-operators find hidden premium lanes."

[Carrier]: "Rates are terrible everywhere."

[You]: "I completely agree. Running blind on public boards is losing money. We find private broker loads that need immediate coverage. If I can show you a route that makes 10% to 15% more than what you are making now, would you give us a try for just 2 loads?"
    ''', language="text")

st.markdown("---")
st.caption("💡 Tip: Keep your voice calm, confident, and do not sound like a standard salesperson.")
