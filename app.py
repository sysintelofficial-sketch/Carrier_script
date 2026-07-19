import streamlit as st

# 1. Page Configuration for Wide Screen (No Scrolling needed)
st.set_page_config(
    page_title="US Carrier Dispatch Dashboard", 
    page_icon="🚛", 
    layout="wide"
)

# Custom Clean Styling
st.markdown("""
    <style>
    .block-container { padding-top: 2rem; padding-bottom: 2rem; }
    .main-title { font-size: 28px; font-weight: bold; color: #1E3A8A; text-align: center; margin-bottom: 20px; }
    .mode-header { font-size: 18px; font-weight: bold; color: #FFFFFF; background-color: #1E40AF; padding: 10px; border-radius: 5px; text-align: center; margin-bottom: 15px; }
    .script-box { background-color: #F8FAFC; border: 1px solid #E2E8F0; padding: 15px; border-radius: 8px; font-family: monospace; font-size: 14px; color: #334155; white-space: pre-wrap; }
    .role-disp { color: #2563EB; font-weight: bold; }
    .role-carr { color: #DC2626; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>🇺🇸 US Carrier Acquisition - Direct Dispatch Matrix</div>", unsafe_allow_html=True)

# -------------------------------------------------------------------------
# STAGE 1: THE QUICK 15-SECOND FILTER (Top of the screen, always visible)
# -------------------------------------------------------------------------
st.markdown("### 🎯 Step 1: The Quick Filter (Opening Call)")
st.info(
    "Purpose: Call start کرتے ہی 15 سیکنڈ میں جانیں کہ کیریئر کے پاس اپنی اتھارٹی (Own Authority) ہے یا نہیں۔"
)

col_opening, col_leased = st.columns(2)

with col_opening:
    st.subheader("🗣️ If Carrier Answers:")
    st.code('''[You]: "Hi [Carrier Name], my name is Ahsan. I will keep this very short. Are you running your trucks under your own independent authority right now, or are you leased onto another company?"''', language="text")

with col_leased:
    st.subheader("🛑 If Leased Onto a Company (Not a Prospect):")
    st.code('''[You]: "Got it! We only work with independent authorities. I appreciate your time, brother. Stay safe out there on the road!"''', language="text")

st.markdown("---")

# -------------------------------------------------------------------------
# STAGE 2: 3 DIFFERENT PITCHING MODES (Side-by-Side Columns for High Visibility)
# -------------------------------------------------------------------------
st.markdown("### 🎛️ Step 2: Choose Your Pitch (Based on Carrier's Response)")
st.caption("سب کچھ سامنے موجود ہے۔ کیریئر کی سچویشن کے مطابق نیچے دیئے گئے 3 کالمز میں سے اسکرپٹ پڑھیں:")

# Creating 3 equal columns so everything stays on one screen
col1, col2, col3 = st.columns(3)

# --- MODE 1: THE MONEY & LANE PITCH ---
with col1:
    st.markdown("<div class='mode-header'>💰 Mode 1: Market Rates & Lanes</div>", unsafe_allow_html=True)
    st.caption("Use when: Carrier wants better paying loads immediately.")
    
    st.code('''
[You]: "Look, I know the spot market is absolute garbage right now and load boards are paying pennies. That is exactly why I called. We work with private broker networks to secure loads before they even touch the public boards."

[Carrier]: "What rates are you getting?"

[You]: "It depends on your equipment, but our goal is to keep you running at a premium net average per week, not just one lucky load. What kind of equipment do you have empty right now, and where do you want to send it?"

[Carrier]: "I have a Dry Van empty in Atlanta."

[You]: "Perfect. I have a clean lane coming out of there. Give me your MC number real quick, let me check your setup, and I will see what we can lock in for Monday."
''', language="text")

# --- MODE 2: THE BACK-OFFICE RELIEF PITCH ---
with col2:
    st.markdown("<div class='mode-header'>👔 Mode 2: Back-Office Relief</div>", unsafe_allow_html=True)
    st.caption("Use when: Owner-Operator is tired of doing paperwork while driving.")
    
    st.code('''
[You]: "I respect that you book your own loads. But driving 11 hours a day and fighting with brokers, filling out packets, and chasing detention pay is exhausting."

[Carrier]: "Yeah, it is a lot of work."

[You]: "Exactly. We act as your dedicated back-office partner. You just focus on driving safely. We handle all broker negotiations, credit checks, setup packets, and factoring invoices. We do the paperwork, you make the money."

[Carrier]: "How much do you charge?"

[You]: "We only take a small [X]% percentage from the loads we book for you. If you do not make money, we do not make money. Let's do a test run. What is your email so I can send the onboarding packet?"
''', language="text")

# --- MODE 3: THE RISK-FREE TRIAL PITCH ---
with col3:
    st.markdown("<div class='mode-header'>🛡️ Mode 3: The 2-Load Trial</div>", unsafe_allow_html=True)
    st.caption("Use when: Carrier says 'I already have a dispatcher' (Objection).")
    
    st.code('''
[You]: "I completely understand you already have a dispatcher. If I were you, I would not trust a stranger over the phone either."

[Carrier]: "Yeah, I am good with my guy."

[You]: "Fair enough. But let me ask you this: if my routing system can find you a 10% to 15% higher rate on your regular lanes, wouldn't you want that extra cash in your pocket?"

[Carrier]: "Well, yeah, if it's real."

[You]: "It is real. Let’s do a 2-load risk-free trial. No contract, no commitment. If I book 2 loads that pay better than your current guy, we talk. If not, you walk away. You have zero downside. What is your MC number so I can prove it to you?"
''', language="text")

# -------------------------------------------------------------------------
# FOOTER NOTES (Quick Reference)
# -------------------------------------------------------------------------
st.markdown("---")
col_foot1, col_foot2 = st.columns(2)
with col_foot1:
    st.success("💡 **US Calling Rule:** لوڑ بورڈ کا نام سن کر اکثر امریکن ڈرائیورز فون کاٹ دیتے ہیں۔ اس لیے بات ہمیشہ ان کے فائدے (Higher Net Revenue) اور ان کا وقت بچانے سے شروع کریں۔")
with col_foot2:
    st.warning("⚠️ **Keep it Natural:** روبوٹ کی طرح اسکرپٹ نہ پڑھیں، بالکل آرام سے جیسے دو کاروباری لوگ آپس میں بات کرتے ہیں۔")
