import streamlit as st

st.set_page_config(page_title="Professional Dispatch Call", layout="centered")

st.markdown("""
    <style>
    .chat-box { background-color: #f9fafb; padding: 15px; border-radius: 8px; border: 1px solid #d1d5db; margin-bottom: 10px; }
    .you { color: #1e40af; font-weight: bold; }
    .carrier { color: #dc2626; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

st.title("📞 Direct Professional Script")

st.markdown("""
<div class='chat-box'>
    <p><span class='you'>[You]:</span> Good morning, [Carrier Name]. This is Ahsan. I’m looking at your carrier profile and see you’re running [Equipment Type]. I’m calling to see if you have capacity for a few high-paying lanes this week?</p>
    
    <p><span class='carrier'>[Carrier]:</span> We’re currently booked, but we’re always looking for better rates. Who are you with?</p>
    
    <p><span class='you'>[You]:</span> I’m an independent dispatcher. I don’t use public boards—I have direct access to private lanes that pay 15% above market average. I’m not asking for a commitment, just a chance to prove the numbers.</p>
    
    <p><span class='carrier'>[Carrier]:</span> Okay, what kind of rates are you talking about for a Dry Van out of Atlanta?</p>
    
    <p><span class='you'>[You]:</span> For that lane, I’m locking in $X per mile consistently. If I can match or beat that today, would you be open to sending me your setup packet?</p>
    
    <p><span class='carrier'>[Carrier]:</span> Send me an email with your details and I’ll take a look.</p>
    
    <p><span class='you'>[You]:</span> Perfect. I’ll send that right now. I’ll keep an eye out for your reply and follow up shortly.</p>
</div>
""", unsafe_allow_html=True)

st.success("💡 Tip: اس میں آپ نے شروع میں ہی بتا دیا کہ آپ کو ان کے ڈیٹا کا پتہ ہے، اس لیے وہ آپ کو سنجیدگی سے لیں گے۔")
