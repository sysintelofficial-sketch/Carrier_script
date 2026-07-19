import streamlit as st

st.set_page_config(page_title="Live Carrier Calling Script", page_icon="📞", layout="centered")

st.title("📞 SIF Cold Calling Matrix")
st.markdown("Use this dynamic workflow during live phone calls. Focus on confidence and pacing.")

# ----------------------------------------------------------------------------------
# STEP 1: THE 15-SECOND HOOK
# ----------------------------------------------------------------------------------
st.header("⚡ Step 1: The Tactical Pattern Interrupter")
st.info("Goal: Break their regular 'spam-dispatcher' defense shield within 15 seconds.")

st.markdown("""
> **You say:** > *"Hi [Carrier Name], my name is Ahsan Khan. I’m the Lead Systems Architect with **System Intelligence Framework**. Look, I’m not calling to sell you standard dispatch services. We run a mathematical routing engine, and our data shows your trucks operating out of **[State]** are likely leaving 15% to 20% yield on the table due to current market capacity mismatches. I want to plug that leak for you this week. Do you have exactly 45 seconds to look at the numbers?"*
""")

# ----------------------------------------------------------------------------------
# STEP 2: OBJECTION HANDLING MATRIX
# ----------------------------------------------------------------------------------
st.header("🛡️ Step 2: Live Objection Handling Matrix")
st.write("Click on the objection the carrier throws at you to see the mathematical counter-attack:")

objection = st.radio(
    "Select the active objection:",
    [
        "Select an objection...",
        "I already have a dispatcher / I book my own loads.",
        "The market is dead right now, freight rates are garbage.",
        "How much do you charge? What's your fee?"
    ]
)

if objection == "I already have a dispatcher / I book my own loads.":
    st.error("⛔ Objection: 'I already have a dispatcher / I book my own loads.'")
    st.markdown("""
    **Your Strategic Response:** *"That’s exactly why I called you. Traditional dispatchers use guesswork and look at public load boards after the loads drop. My framework runs deterministic models that synchronize live EIA Diesel Indexes and USDA capacity trends. We see where the high-paying loads are shifting **before** they hit the board. Let me prove it: I will run our fleet routing engine for **2 Test Loads completely free**. No contract, no cut. If my math beats your current dispatcher's numbers, we talk. If not, you keep the profit and walk away. What equipment are your drivers running this Monday?"*
    """)

elif objection == "The market is dead right now, freight rates are garbage.":
    st.error("⛔ Objection: 'The market is dead right now, freight rates are garbage.'")
    st.markdown("""
    **Your Strategic Response:** *"You are 100% correct, the spot market is brutal right now. But here is the secret: even in a dead market, there are micro-lanes with capacity deficits where brokers are desperate and forced to pay premium rates. Standard dispatchers can’t find them because they don't look at the analytics. We isolate these pricing arbitrage points mathematically. Our system targets yield optimization, not just mileage. Let me take the risk—let me book just 2 loads for you under your own authority. If you don't like the rate, you just say NO. Fair enough?"*
    """)

elif objection == "How much do you charge? What's your fee?":
    st.error("⛔ Objection: 'How much do you charge? What's your fee?'")
    st.markdown("""
    **Your Strategic Response:** *"Right now, **zero dollars**. I want to build trust first. I am giving you a **2-Load Free Trial** with absolutely no contracts and no obligations. Once we prove our system out-negotiates your current rates, our long-term rate is a flat 7% premium management fee. But you don't owe me a dime until those first two high-yielding loads are successfully delivered and paid. Let's set up the trial today—what's the best email to send our system activation link?"*
    """)

# ----------------------------------------------------------------------------------
# STEP 3: THE CLOSE & DATA INGESTION
# ----------------------------------------------------------------------------------
if objection != "Select an objection...":
    st.header("🎯 Step 3: Secure the Close (Onboarding Ingestion)")
    st.success("They agreed! Transition smoothly to secure the asset pack:")
    st.markdown("""
    **You say:** *"Perfect. To initialize the routing optimization engine for Monday, I'm sending you a secure setup link from **contact@sysintelofficial.com**. Reply to that with your W9, COI, and MC Letter. Once my data team verifies your profile, we'll line up your first premium load option. Let's get this fleet optimized!"*
    """)
