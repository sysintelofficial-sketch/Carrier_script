import streamlit as st

# Page Configuration
st.set_page_config(page_title="Carrier Acquisition Pipeline", page_icon="📞", layout="wide")

# Styling for better readability
st.markdown("""
    <style>
    .main-title { font-size:32px !important; font-weight: bold; color: #1E3A8A; text-align: center; }
    .mode-box { background-color: #F3F4F6; padding: 20px; border-radius: 10px; border-left: 5px solid #2563EB; margin-bottom: 20px; }
    .dialogue-text { font-size: 18px !important; font-style: italic; color: #111827; background-color: #FFFFFF; padding: 15px; border-radius: 5px; border: 1px solid #D1D5DB; }
    .urdu-tip { font-size: 16px !important; color: #047857; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>🚛 FMCSA Carrier Acquisition & Live Calling Matrix</div>", unsafe_allow_html=True)
st.write("Monday سے کالز شروع کرنے کے لیے نیچے دیے گئے 5 مختلف موڈز میں سے کسی بھی ایک کو کیریئر کے مزاج کے مطابق منتخب کریں۔")

# ----------------------------------------------------------------------------------
# SIDEBAR NAVIGATION
# ----------------------------------------------------------------------------------
st.sidebar.markdown("### 🎛️ Select Pitching Mode")
current_mode = st.sidebar.radio(
    "کال کرنے کا موڈ منتخب کریں:",
    [
        "Mode 1: The Analytical Systems Pitch (ڈیٹا اور ریاضی کا طریقہ)",
        "Mode 2: The Aggressive Hot-Lane Pitch (ہائی ریٹ لین کا طریقہ)",
        "Mode 3: The 2-Load Risk-Free Trial (فری ٹرائل کا طریقہ)",
        "Mode 4: Full Back-Office Relief Pitch (کمپنی مینجمنٹ کا طریقہ)",
        "Mode 5: The Conversational Partnership Pitch (سادہ اور مخلص طریقہ)"
    ]
)

# ----------------------------------------------------------------------------------
# MODE 1: THE ANALYTICAL SYSTEMS PITCH
# ----------------------------------------------------------------------------------
if "Mode 1" in current_mode:
    st.header("🧠 Mode 1: The Analytical Systems Pitch")
    st.markdown("<p class='urdu-tip'>💡 یہ کب استعمال کریں: جب آپ کسی ایسے کیریئر سے بات کر رہے ہوں جو مارکیٹ کے حالات سے تنگ آ چکا ہو اور سنجیدہ بات سننا چاہتا ہو۔</p>", unsafe_allow_html=True)
    
    st.markdown("<div class='mode-box'>", unsafe_allow_html=True)
    st.subheader("1️⃣ Intro Hook (پہلے 15 سیکنڈ):")
    st.markdown("""<div class='dialogue-text'>
    "Hi [Carrier Name], my name is Ahsan. I’m the Lead Systems Architect at System Intelligence Framework. Look, I'm not a regular broker or a standard dispatcher calling to waste your time. We run a mathematical routing framework that maps real-time capacity deficits in your lane. Right now, our data shows your trucks running out of [State] are leaving up to 15% revenue on the table. Do you have exactly 45 seconds to let me explain how we fix that?"
    </div>""", unsafe_allow_html=True)
    
    st.subheader("2️⃣ The Value Pitch (اصل بات چیت):")
    st.markdown("""<div class='dialogue-text'>
    "Most dispatchers just guess and look at public load boards after prices drop. We don't guess—we run predictive market math. We locate high-paying micro-lanes and match them with your equipment before the market gets flooded. We handle your entire logistics pipeline, optimize your cost-per-mile efficiency, and keep your fleet moving smoothly. You drive, we maximize the yield."
    </div>""", unsafe_allow_html=True)

    st.subheader("3️⃣ The Close (ڈیل فائنل کرنا):")
    st.markdown("""<div class='dialogue-text'>
    "I want to dispatch your first truck on Monday to show you the numbers. What kind of equipment do you have ready, and what is your minimum rate per mile requirement?"
    </div>""", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------------------------------------------------------------
# MODE 2: THE AGGRESSIVE HOT-LANE PITCH
# ----------------------------------------------------------------------------------
elif "Mode 2" in current_mode:
    st.header("🔥 Mode 2: The Aggressive Hot-Lane Pitch")
    st.markdown("<p class='urdu-tip'>💡 یہ کب استعمال کریں: جب کیریئر جلدی میں ہو اور اسے صرف اچھے ریٹ (Rates) اور بہترین روٹس (Lanes) سے مطلب ہو۔</p>", unsafe_allow_html=True)
    
    st.markdown("<div class='mode-box'>", unsafe_allow_html=True)
    st.subheader("1️⃣ Intro Hook (پہلے 15 سیکنڈ):")
    st.markdown("""<div class='dialogue-text'>
    "Hey [Carrier Name], this is Ahsan with System Intelligence Framework. I'm calling because our routing engine just triggered a capacity alert for your area. Brokers are struggling to move freight in your lanes right now, which means we have leverage to demand premium rates. I need a reliable carrier under their own authority to plug into this lane immediately. Are you currently loaded or looking for a high-paying run?"
    </div>""", unsafe_allow_html=True)
    
    st.subheader("2️⃣ The Value Pitch (اصل بات چیت):")
    st.markdown("""<div class='dialogue-text'>
    "We specialize in finding pricing arbitrage. Right now, standard load boards are paying garbage, but our private broker network and data algorithms isolate contract loads that need immediate coverage. As your dedicated dispatcher, we don't just book a load; we chain your back-haul together so your truck never runs empty or deadheads for pennies."
    </div>""", unsafe_allow_html=True)

    st.subheader("3️⃣ The Close (ڈیل فائنل کرنا):")
    st.markdown("""<div class='dialogue-text'>
    "Let’s get your truck locked into this high-yield lane before another fleet takes it. What is your MC number so I can check your setup status?"
    </div>""", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------------------------------------------------------------
# MODE 3: THE 2-LOAD RISK-FREE TRIAL
# ----------------------------------------------------------------------------------
elif "Mode 3" in current_mode:
    st.header("🛡️ Mode 3: The 2-Load Risk-Free Trial")
    st.markdown("<p class='urdu-tip'>💡 یہ کب استعمال کریں: جب کیریئر کہے کہ 'میرا اپنا ڈیسپیچر ہے' یا 'میں خود لوڈ بک کرتا ہوں'۔ یہ ان کا دفاعی شیلڈ توڑنے کا بہترین طریقہ ہے۔</p>", unsafe_allow_html=True)
    
    st.markdown("<div class='mode-box'>", unsafe_allow_html=True)
    st.subheader("1️⃣ Intro Hook (پہلے 15 سیکنڈ):")
    st.markdown("""<div class='dialogue-text'>
    "I completely understand you book your own loads / have a dispatcher. Honestly, if I were you, I wouldn’t trust a stranger over the phone either. That’s exactly why I’m not asking you to sign anything or switch to me. I want to offer you a 2-Load Risk-Free Test Run. No contracts, no commitments, and zero upfront fees. If my routing engine can't beat your current rates, you walk away and don't owe me a dime. Fair enough?"
    </div>""", unsafe_allow_html=True)
    
    st.subheader("2️⃣ The Value Pitch (اصل بات چیت):")
    st.markdown("""<div class='dialogue-text'>
    "Think of us as your backup intelligence team. You keep doing what you are doing, but let me run your equipment through our framework for just two loads. We will handle the heavy negotiation with brokers, set up the detention tracking, and make sure you get premium access. If we perform, we talk about a long-term dispatch partnership. If we don’t, you keep 100% of the profit from those two loads and we part ways as friends."
    </div>""", unsafe_allow_html=True)

    st.subheader("3️⃣ The Close (ڈیل فائنل کرنا):")
    st.markdown("""<div class='dialogue-text'>
    "There is absolutely no downside for your business. I'll send a secure onboarding link from contact@sysintelofficial.com. What's the best email to send that over so we can activate your trial for Monday?"
    </div>""", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------------------------------------------------------------
# MODE 4: FULL BACK-OFFICE RELIEF PITCH
# ----------------------------------------------------------------------------------
elif "Mode 4" in current_mode:
    st.header("👔 Mode 4: Full Back-Office Relief Pitch")
    st.markdown("<p class='urdu-tip'>💡 یہ کب استعمال کریں: جب آپ کسی ایسے اکیلے اونر-آپریٹر (Owner-Operator) سے بات کر رہے ہوں جو ڈرائیونگ بھی خود کرتا ہو اور پیپر ورک اور فیکٹرنگ سے تھک چکا ہو۔</p>", unsafe_allow_html=True)
    
    st.markdown("<div class='mode-box'>", unsafe_allow_html=True)
    st.subheader("1️⃣ Intro Hook (پہلے 15 سیکنڈ):")
    st.markdown("""<div class='dialogue-text'>
    "Hi [Carrier Name], this is Ahsan from System Intelligence Framework. I see you are running an independent operation, and honestly, driving 11 hours a day while trying to fight with brokers, handle invoicing, and manage compliance is a nightmare. I’m calling to let you know that you don't have to do it alone anymore. We act as your complete back-office dispatch partner so you can just focus on the road safely."
    </div>""", unsafe_allow_html=True)
    
    st.subheader("2️⃣ The Value Pitch (اصل بات چیت):")
    st.markdown("""<div class='dialogue-text'>
    "When you partner with us, we take over everything. We set up your packets with top-tier brokers, handle the factoring invoicing instantly so you get paid within 24 hours, track layovers, and fight for your detention pay down to the last dollar. We use advanced route optimization to schedule your weekly runs seamlessly, ensuring you get back home to your family on time without sacrificing your profit margins."
    </div>""", unsafe_allow_html=True)

    st.subheader("3️⃣ The Close (ڈیل فائنل کرنا):")
    st.markdown("""<div class='dialogue-text'>
    "Let us take the administrative weight off your shoulders this week. Let’s get your profile set up in our dispatch system today. Can you share your MC number with me to initiate the paperwork?"
    </div>""", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------------------------------------------------------------
# MODE 5: THE CONVERSATIONAL PARTNERSHIP PITCH (NEW SIMPLE MODE)
# ----------------------------------------------------------------------------------
elif "Mode 5" in current_mode:
    st.header("🤝 Mode 5: The Conversational Partnership Pitch")
    st.markdown("<p class='urdu-tip'>💡 یہ کب استعمال کریں: یہ ایک بالکل سادہ، پروفیشنل اور مخلصانہ طریقہ ہے۔ جب آپ کیریئر پر کوئی دباؤ ڈالے بغیر براہِ راست پارٹنرشپ کی بات کرنا چاہیں۔</p>", unsafe_allow_html=True)
    
    st.markdown("<div class='mode-box'>", unsafe_allow_html=True)
    st.subheader("1️⃣ Intro Hook (پہلے 15 سیکنڈ):")
    st.markdown("""<div class='dialogue-text'>
    "Hi [Carrier Name], my name is Ahsan from System Intelligence Framework. I'll keep it short: I’m a professional truck dispatcher, and I’m currently looking to partner with a few reliable carriers under their own authority to help them book high-paying loads."
    </div>""", unsafe_allow_html=True)
    
    st.subheader("2️⃣ The Value Pitch (اصل بات چیت):")
    st.markdown("""<div class='dialogue-text'>
    "I know the market is tough right now, so we handle all the heavy lifting—like tracking premium micro-lanes, negotiating with brokers, and managing setup packets—so you can just focus on driving without the stress of public load boards."
    </div>""", unsafe_allow_html=True)

    st.subheader("3️⃣ The Close (ڈیل فائنل کرنا):")
    st.markdown("""<div class='dialogue-text'>
    "I'm not asking for any upfront commitments. I just wanted to see if you are currently looking for a dedicated dispatcher, or if you're open to seeing how we can maximize your weekly revenue starting Monday?"
    </div>""", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------------------------------------------------------------
# LIVE COUNTER-ATTACK/OBJECTION HANDLING (QUICK REFERENCE)
# ----------------------------------------------------------------------------------
st.sidebar.markdown("---")
st.sidebar.markdown("### 🛡️ Quick Objection Counter")
live_obj = st.sidebar.selectbox(
    "کال پر آنے والے اعتراض کا فوری جواب پائیں:",
    ["Select Objection...", "Your fee is too high!", "I don't trust third-party dispatchers."]
)

if live_obj == "Your fee is too high!":
    st.sidebar.warning("💬 Say: 'I understand 7% sounds standard, but a cheap 5% dispatcher bookings garbage loads actually costs you thousands in deadhead miles. Our math guarantees a higher net yield per week. We don't cost you money, we make you money.'")
elif live_obj == "I don't trust third-party dispatchers.":
    st.sidebar.warning("💬 Say: 'I respect that completely. That’s why everything we do is under YOUR authority. The broker pays YOU directly. We never touch your money. We just send the setup packets and optimize the math.'")
