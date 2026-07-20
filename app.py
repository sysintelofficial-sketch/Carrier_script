import streamlit as st

st.set_page_config(page_title="Dispatch Script", layout="centered")

st.title("📞 Professional Dispatcher Script")

# Dialogue Container
st.markdown("""
<div style="background-color: #f0f2f6; padding: 20px; border-radius: 10px;">
    <b>[You]:</b> Good morning, [Carrier Name]. This is Ahsan. I’ve been reviewing your fleet data and I’m reaching out to see if you have open capacity for some premium lanes this week?
    <br><br>
    <b>[Carrier]:</b> We are always looking for better freight. What kind of lanes are you working with?
    <br><br>
    <b>[You]:</b> I focus on private, high-paying lanes that don’t hit the public load boards. I’m not looking for a contract today—I just want to prove my value with one or two loads.
    <br><br>
    <b>[Carrier]:</b> That sounds interesting. What are your average rates for [Equipment Type]?
    <br><br>
    <b>[You]:</b> I’m consistently securing 15% above the current market average. If I can prove that on your next load, would you be open to a formal setup?
    <br><br>
    <b>[Carrier]:</b> Fair enough. Send over your company info and we can look into it.
    <br><br>
    <b>[You]:</b> Perfect. I will email that to you immediately and follow up with a quick call once you've had a chance to review it.
</div>
""", unsafe_allow_html=True)

# Footer for quick reference
st.markdown("---")
st.caption("Keep it simple, professional, and straight to the point.")
