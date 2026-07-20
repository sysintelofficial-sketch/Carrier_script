import streamlit as st

st.set_page_config(page_title="Carrier Pitch", layout="centered")

st.markdown("""
    <style>
    .script-box { background-color: #f8f9fa; padding: 20px; border-radius: 12px; 
                  border-left: 6px solid #2563eb; font-size: 20px; color: #1e293b; }
    </style>
""", unsafe_allow_html=True)

st.title("🚛 Dispatcher Talk")

# 1. Quick Intro & Qualification
st.subheader("Step 1: The Intro")
st.markdown("""
<div class='script-box'>
<b>[You]:</b> "Hi [Carrier Name], this is Ahsan. I’m a local dispatcher. I’m just calling to see if you’re running under your own authority or leased onto a company?"
</div>
""", unsafe_allow_html=True)

# 2. The Hook (Value Addition)
st.subheader("Step 2: The Pitch")
st.markdown("""
<div class='script-box'>
<b>[You]:</b> "Got it. Look, I’m trying to build a small network of reliable carriers. I’m not asking for a contract—I just want to prove I can find you better-paying loads than what's on the board. Do you have a truck available, and would you be open to trying a couple of loads with me?"
</div>
""", unsafe_allow_html=True)

# 3. Closing (The Call to Action)
st.subheader("Step 3: The Next Step")
st.markdown("""
<div class='script-box'>
<b>[You]:</b> "Great. Let’s do a quick trial. What’s your MC number so I can check your setup, and what’s the best email to send the details over?"
</div>
""", unsafe_allow_html=True)

st.info("نکۃ: اگر وہ کہیں 'ہمیں ضرورت نہیں'، تو بس کہیں: 'کوئی بات نہیں، میں آپ کا نمبر سیو کر لیتا ہوں، شاید مستقبل میں کبھی ضرورت پڑے۔ اپنا خیال رکھیں، خدا حافظ۔'")
