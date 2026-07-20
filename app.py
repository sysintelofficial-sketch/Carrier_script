import streamlit as st

st.set_page_config(page_title="Professional Dispatcher Script", layout="centered")

st.markdown("""
    <style>
    .dialogue-box { background-color: #ffffff; padding: 20px; border-radius: 10px; border: 1px solid #ddd; }
    .you-line { color: #1e3a8a; font-weight: bold; margin-bottom: 10px; }
    .carrier-line { color: #b91c1c; font-weight: bold; margin-bottom: 10px; }
    </style>
""", unsafe_allow_html=True)

st.title("📞 Quick Dispatcher Script")

st.markdown("""
<div class="dialogue-box">
    <div class="you-line">
        [You]: "Hi [Carrier Name], this is Ahsan. I’m a professional dispatcher and I'm calling to see if you have any need for extra freight support right now?"
    </div>
    
    <div class="carrier-line">
        [Carrier]: "Not really, we're doing okay on our own. Why are you calling?"
    </div>
    
    <div class="you-line">
        [You]: "I understand. I’m just building my network and I secure premium rates for my carriers. If you ever need to fill a gap or get a better rate, would you like me to send you my details?"
    </div>
    
    <div class="carrier-line">
        [Carrier]: "Sure, send it over, I'll take a look if we get stuck."
    </div>
    
    <div class="you-line">
        [You]: "Great, I'll email my info right now. I’ll follow up in a few days to see if you need any help. Thanks for your time!"
    </div>
</div>
""", unsafe_allow_html=True)

st.sidebar.info("💡 Keep it quick. If they say no, hang up politely immediately.")
