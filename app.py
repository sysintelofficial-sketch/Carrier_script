import streamlit as st

# Qualification Section Heading
st.header("🎯 Quick Carrier Qualification Flow")
st.write("कॉल शुरू करते ही कैरिअर का मिजाज और जरूरत भांपने के लिए नीचे दिए गए ऑप्शन्स पर क्लिक करें:")

st.markdown("---")

# STEP 1: Introduction Hook
st.subheader("🗣️ The Opening Question")
st.code(
    '"Hi [Carrier Name], this is Ahsan. I’ll be incredibly brief. Are you currently running your trucks under your own authority, or are you leased onto a company right now?"', 
    language="text"
)

# Interactive Selector for Step 1
step_1_answer = st.selectbox(
    "कैरिअर का जवाब चुनें (Step 1):",
    ["-- कैरिअर का जवाब चुनें --", "Yes, Own Authority", "No, Leased onto a company"]
)

# Logic based on Step 1
if step_1_answer == "Yes, Own Authority":
    st.success("✅ Good Prospect! Proceed to Step 2.")
    
    # STEP 2: Dispatcher Check
    st.subheader("🗣️ The Follow-up Question")
    st.code(
        '"Got it. And are you handling all your own load bookings yourself, or do you work with a dedicated dispatch team to keep your fleet moving?"', 
        language="text"
    )
    
    step_2_answer = st.selectbox(
        "कैरिअर का जवाब चुनें (Step 2):",
        ["-- कैरिअर का जवाब चुनें --", "I do it myself / I already have a dispatcher", "I am looking for loads / I need help"]
    )
    
    # Final Dialogues based on Scenario
    if step_2_answer == "I do it myself / I already have a dispatcher":
        st.info("🪵 Scenario A: Perfect for Mode 3 (2-Load Trial)")
        st.code(
            '"That’s completely fair. Most successful owner-operators prefer keeping control. Just out of curiosity, if there was a routing framework that could consistently pull 10% to 15% higher rates on your current lanes, would you even be open to looking at a free 2-load trial, or are you 100% satisfied with your current net weekly revenue?"', 
            language="text"
        )
        
    elif step_2_answer == "I am looking for loads / I need help":
        st.warning("🔥 Scenario B: Perfect for Mode 2 (Hot-Lane Pitch)")
        st.code(
            '"I completely understand, the spot market is brutal right now. That is exactly why I called. We specialize in mapping real-time capacity deficits to grab contract loads before they hit public boards. Let’s not waste time—what equipment do you have empty right now, and where are you trying to send it?"', 
            language="text"
        )

elif step_1_answer == "No, Leased onto a company":
    st.error("❌ Not a Prospect: Leased कैरिअर्स खुद लोड बुक नहीं कर सकते। टाइम बचाएं और कॉल प्यार से खत्म करें।")
    st.code(
        '"Got it! We specifically work with independent authorities, but I wish you the best of luck on the road. Stay safe out there!"', 
        language="text"
    )
