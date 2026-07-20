import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Ahsan Khan | Dispatch Pro", page_icon="🚛", layout="wide")

# Custom CSS for a professional, distraction-free UI
st.markdown("""
    <style>
    .main-title { font-size: 28px; font-weight: bold; color: #1E3A8A; text-align: center; margin-bottom: 20px; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #1E40AF; color: white; }
    .script-box { background-color: #F1F5F9; padding: 20px; border-radius: 10px; border-left: 5px solid #1E40AF; font-size: 16px; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>🚛 Professional Carrier Acquisition Suite</div>", unsafe_allow_html=True)

# 2. The 15-Second Qualifier (Always visible at the top)
st.subheader("🎯 Step 1: Initial Qualifier")
with st.expander("Click to view Qualifier Script", expanded=True):
    st.markdown("""
    **[You]:** 'Hi, is this [Carrier Name]? This is Ahsan, I’ll keep this very brief. Are you currently running your trucks under your own authority, or are you leased onto another company?'
    
    *   **If Leased:** 'Understood, I appreciate your time. We only partner with independent carriers. Stay safe out there!'
    *   **If Independent:** 'Great—are you looking to improve your rate-per-mile or just looking for back-office support right now?'
    """)

st.markdown("---")

# 3. Sequencing the Pitch (Using Tabs to keep it clean)
st.subheader("🎛️ Step 2: Pitch Strategy")
tab1, tab2, tab3 = st.tabs(["💰 Market Rates & Lane Optimizer", "👔 Back-Office Efficiency", "🤝 Relationship Builder (Long-Term)"])

with tab1:
    st.markdown("### Focus: Increasing Net Revenue")
    st.markdown("""
    **[You]:** 'I’ve been tracking the lanes in your region. The current spot market is tight, but I’ve built a network that secures premium freight before it hits public boards. If I could get you a consistent 15-20% higher rate-per-mile on your Dry Van, would you be open to a 2-load trial?'
    """)

with tab2:
    st.markdown("### Focus: Time & Operational Relief")
    st.markdown("""
    **[You]:** 'I know how draining it is to drive 11 hours and then spend your nights fighting with brokers and chasing detention pay. I want to handle all that paperwork—setup packets, credit checks, and invoices—so you can just focus on driving and making money. Does that sound like the kind of help you need?'
    """)

with tab3:
    st.markdown("### Focus: The Professional Partnership (High-Trust)")
    st.markdown("""
    **[You]:** 'Look, there are a thousand dispatchers calling you today, and I know trust is hard to come by over the phone. I’m not looking to just book one load. I’m looking to become your dedicated back-office partner. I’d like to prove my value by booking your next two loads exactly where you want to go. If I don't beat your current profit margin, we go our separate ways—no hard feelings. What’s your MC number so I can check your setup?'
    """)

# 4. Closing the Deal (Next Steps)
st.markdown("---")
st.subheader("🚀 Step 3: Closing & Onboarding")
if st.button("Generate Closing Sequence"):
    st.success("""
    **[Closing Protocol]:**
    1. **Verify:** 'I’ve got your MC number. I’m going to run a quick setup check.'
    2. **Agreement:** 'I’ll send over our simple service agreement via DocuSign to your email. No long-term commitments.'
    3. **Action:** 'What is the best email to reach you at? I'll send that over now, and let's get you loaded for tomorrow morning.'
    """)
