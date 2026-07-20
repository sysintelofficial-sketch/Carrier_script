import streamlit as st

# Page Configuration
st.set_page_config(page_title="Dispatch Pro", layout="centered")

# Custom Styling
st.markdown("""
    <style>
    .script-box { background-color: #ffffff; padding: 20px; border-radius: 10px; 
                  border: 2px solid #1E40AF; font-size: 18px; color: #1E293B; }
    .header-text { color: #1E40AF; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

st.title("🚛 Dispatcher Quick-Pitch")

# Step-by-Step Logic
# 1. First Contact (The Qualifier)
st.markdown("<h3 class='header-text'>Step 1: The Qualifier (Is he independent?)</h3>", unsafe_allow_html=True)
with st.container():
    st.markdown("""
    <div class='script-box'>
    <b>[You]:</b> "Good morning! This is Ahsan. I’m calling to see if you’re running your own authority right now, or are you leased onto another company?"
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# 2. If Independent (The Pitch)
st.markdown("<h3 class='header-text'>Step 2: The Value Hook (Only if Independent)</h3>", unsafe_allow_html=True)
with st.container():
    st.markdown("""
    <div class='script-box'>
    <b>[You]:</b> "Great. Look, I’m not looking to waste your time with a contract. I’m a dedicated dispatcher, and I’m just looking to add a reliable truck to my network. If I can book you a load that pays better than what you’re seeing on the boards right now, would you be open to giving me a shot?"
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# 3. The Close (The "Trial" Deal)
st.markdown("<h3 class='header-text'>Step 3: The Close (Action)</h3>", unsafe_allow_html=True)
with st.container():
    st.markdown("""
    <div class='script-box'>
    <b>[You]:</b> "Fair enough. Let's do a two-load trial—zero commitment. If I don't beat your current profit, we don't work together. What’s your MC number, and let’s see what I can get you for tomorrow?"
    </div>
    """, unsafe_allow_html=True)

st.sidebar.success("💡 Keep it calm. Don't rush. You are a business partner, not a salesman.")
