import streamlit as st

# Page Configuration
st.set_page_config(page_title="Dispatch Pro Practice", layout="centered")

# Styling
st.markdown("""
    <style>
    .step-box { background-color: #ffffff; padding: 15px; border-radius: 10px; border: 2px solid #1e40af; margin-bottom: 15px; }
    .you-text { color: #1e3a8a; font-size: 20px; font-weight: bold; }
    .carrier-text { color: #991b1b; font-size: 18px; font-weight: 500; }
    </style>
""", unsafe_allow_html=True)

st.title("🚛 Professional Pitch Trainer")

# Dialogue steps
dialogue = [
    {"role": "You", "text": "Hi [Name], this is Ahsan. I'm a professional dispatcher—are you looking for extra freight support right now?", "color": "#dbeafe"},
    {"role": "Carrier", "text": "Not really, we're doing okay on our own. Why are you calling?", "color": "#fee2e2"},
    {"role": "You", "text": "I understand. I work with private lanes that pay above market average. If you ever need a hand, should I send you my info for your files?", "color": "#dbeafe"},
    {"role": "Carrier", "text": "Sure, send it over, I'll take a look if we get stuck.", "color": "#fee2e2"},
    {"role": "You", "text": "Perfect, I'll email that right now. I'll follow up in a few days. Thanks for your time!", "color": "#dbeafe"}
]

st.subheader("Practice your flow line-by-line:")

# Displaying each line with a practice focus
for i, line in enumerate(dialogue):
    with st.container():
        st.markdown(f"""
        <div class="step-box" style="border-color: {'#1e3a8a' if line['role'] == 'You' else '#b91c1c'}">
            <p style="color: #64748b; font-size: 12px; margin-bottom: 5px;">{line['role'].upper()}</p>
            <p class="{'you-text' if line['role'] == 'You' else 'carrier-text'}">{line['text']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Adding a button to focus on that specific line
        if st.button(f"Focus/Read Line {i+1}", key=f"btn_{i}"):
            st.info(f"Take your time. Read this line clearly: '{line['text']}'")

st.markdown("---")
st.write("💡 **Tip:** ہر لائن کو اونچی آواز میں پڑھیں اور اپنے لہجے کو آرام دہ اور پُراعتماد رکھیں۔")
