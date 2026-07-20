import os
# Force Streamlit to run on Port 8502 to avoid port conflicts
os.environ["STREAMLIT_SERVER_PORT"] = "8502"
os.environ["STREAMLIT_SERVER_HEADLESS"] = "true"

import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import re
import math
import io

# --- TEXT TO SPEECH IMPORT ---
from gtts import gTTS

# --- ZOHO EMAIL IMPORTS ---
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

# Dashboard Configuration
st.set_page_config(page_title="FMCSA Master Dashboard", page_icon="🚛", layout="wide")

# ----------------------------------------------------------------------------------
# 📧 ZOHO EMAIL SENDING FUNCTION (NO DATABASE REQUIRED)
# ----------------------------------------------------------------------------------
def send_direct_zoho_email(recipient_email, subject, body_text):
    sender_email = "contact@sysintelofficial.com"
    sender_password = "xVceJUzDTq9v"  # Aapka Zoho App Password
    
    msg = MIMEMultipart()
    msg["Subject"] = Header(subject, 'utf-8')
    msg["From"] = f"System Intelligence Framework <{sender_email}>"
    msg["To"] = recipient_email
    
    msg.attach(MIMEText(body_text, "plain", "utf-8"))
    
    try:
        with smtplib.SMTP_SSL("smtp.zoho.com", 465) as server:
            server.login(sender_email, sender_password)
            server.send_message(msg)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

# ----------------------------------------------------------------------------------
# 🎨 ADVANCED CUSTOM CSS & PERMANENT FIXES
# ----------------------------------------------------------------------------------
st.markdown("""
<style>
/* Target all possible Streamlit Copy Buttons inside Code Blocks */
[data-testid="stCodeBlock"] button, 
[data-testid="stCopyButton"],
button[title="Copy to clipboard"],
button[aria-label="Copy to clipboard"] {
    opacity: 1 !important; 
    visibility: visible !important;
    background-color: #2D2D2D !important; 
    color: #FFFFFF !important; 
    border-radius: 5px !important;
    border: 1px solid #000000 !important;
    right: 5px !important;
    top: 5px !important;
    z-index: 10 !important;
}
[data-testid="stCodeBlock"] button:hover, 
[data-testid="stCopyButton"]:hover {
    background-color: #000000 !important; 
    color: #FFD700 !important; 
}

/* Print Layout Optimization Styling */
@media print {
    body * {
        visibility: hidden;
    }
    .print-area, .print-area * {
        visibility: visible;
    }
    .print-area {
        position: absolute;
        left: 0;
        top: 0;
        width: 100%;
        font-family: 'Arial', sans-serif;
        color: #2D3748 !important;
        line-height: 1.6 !important;
    }
}

/* Stage 4 & 5 Custom Styling Components */
.secure-card {
    background-color: #f8fafc !important;
    border: 1px solid #cbd5e1 !important;
    padding: 15px !important;
    border-radius: 8px !important;
    margin-bottom: 15px !important;
}
.badge-blue {
    background-color: #0284c7 !important;
    color: white !important;
    padding: 3px 10px !important;
    border-radius: 12px !important;
    font-size: 0.85rem !important;
    font-weight: 700 !important;
}
.badge-green {
    background-color: #16a34a !important;
    color: white !important;
    padding: 3px 10px !important;
    border-radius: 12px !important;
    font-size: 0.85rem !important;
    font-weight: 700 !important;
}

/* 🎧 LIVE CALL SCRIPT CUSTOM CSS */
.chat-box { 
    padding: 15px 20px; 
    border-radius: 12px; 
    font-size: 22px !important; 
    line-height: 1.6;
    margin-bottom: 15px;
    box-shadow: 2px 2px 8px rgba(0,0,0,0.05);
}
.you-box { background-color: #e3f2fd; color: #0d47a1; border-left: 6px solid #1976d2; }
.carrier-box { background-color: #ffebee; color: #b71c1c; border-left: 6px solid #d32f2f; }
</style>
""", unsafe_allow_html=True)
# ----------------------------------------------------------------------------------

st.title("🚛 FMCSA Executive Dashboard")
st.markdown("This system displays data strictly for **100% Active**, **Authorized For Hire**, **Interstate**, and **USA Only** carriers.")

# File Uploader in Sidebar
st.sidebar.header("📂 Saved File Manager")
uploaded_file = st.sidebar.file_uploader("Upload a previously saved CSV file:", type=["csv"])

@st.cache_data
def load_data():
    try:
        df = pd.read_csv("Master_Cleaned_Data.csv", dtype=str)
        return df
    except FileNotFoundError:
        return None

# Load data based on user action
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, dtype=str)
    st.sidebar.success("✅ Displaying data from your uploaded file!")
else:
    df = load_data()

if df is None:
    st.error("❌ 'Master_Cleaned_Data.csv' not found! Please run your 'cleaner.py' first.")
    st.stop()

# ----------------------------------------------------------------------------------
# 🛡️ ADVANCED MULTI-FILE BLACKLIST CLEANER
# ----------------------------------------------------------------------------------
st.sidebar.markdown("---")
st.sidebar.header("🚫 Zero-Tolerance Bulk Cleaner")
blacklist_files = st.sidebar.file_uploader(
    "Upload Blacklist CSVs (Select one or multiple together):", 
    type=["csv"], 
    accept_multiple_files=True
)

if blacklist_files and df is not None:
    all_blacklist_dots = set()
    for file in blacklist_files:
        try:
            df_bad = pd.read_csv(file, dtype=str)
            bad_dot_col = next((c for c in df_bad.columns if "DOT" in str(c).upper()), None)
            if bad_dot_col:
                bad_dots = df_bad[bad_dot_col].astype(str).str.split('.').str[0].str.strip().dropna().unique()
                all_blacklist_dots.update(bad_dots)
        except Exception as e:
            st.sidebar.error(f"Error reading file {file.name}: {e}")
            
    if all_blacklist_dots:
        if 'DOT_NUMBER' in df.columns:
            master_dots_cleaned = df['DOT_NUMBER'].astype(str).str.split('.').str[0].str.strip()
            df = df[~master_dots_cleaned.isin(all_blacklist_dots)]

st.sidebar.markdown("---")

# Base Filtering for Active Carriers ONLY
if 'STATUS_CODE' in df.columns:
    df = df[df['STATUS_CODE'].astype(str).str.strip().str.upper() == 'A']

if 'ADD_DATE' in df.columns:
    df['REG_DATE_PARSED'] = pd.to_datetime(df['ADD_DATE'], errors='coerce')
    current_date = pd.Timestamp.now()
    df['AGE_YEARS'] = (current_date - df['REG_DATE_PARSED']).dt.days / 365.25
else:
    df['AGE_YEARS'] = 0.0

if 'TOTAL_DRIVERS' in df.columns:
    df['DRIVERS_COUNT'] = pd.to_numeric(df['TOTAL_DRIVERS'], errors='coerce').fillna(0)
else:
    df['DRIVERS_COUNT'] = 0

# ----------------------------------------------------------------------------------
# 🎯 1. SIDEBAR FILTERS & SMART TOGGLES
# ----------------------------------------------------------------------------------
st.sidebar.header("🎯 Advanced Filters")
age_filter = st.sidebar.selectbox(
    "Select Carrier Market Age:",
    ["🌐 Any Market Age", "👶 0-1 Years (New)", "🚀 1-2 Years (Growing)", "💼 2-5 Years (Experienced)", "🏛️ 6-10 Years (Established)"]
)

driver_filter = st.sidebar.selectbox(
    "Select Driver Count:",
    ["🌐 Any Number of Drivers", "🚖 3 to 5 Drivers", "👤 Exactly 1 Driver", "👥 Exactly 2 Drivers", "👥 Exactly 3 Drivers", "👥 Exactly 4 Drivers", "👥 Exactly 5 Drivers", "👥 6-10 Drivers", "🪪 11-50 Drivers"]
)

zone_options = ["🌐 All Zones"] + [f"📍 Zone {i}" for i in range(10)]
zone_filter = st.sidebar.selectbox("Select Zone (Based on ZIP Code):", zone_options)

# Create the filtered base dataframe first!
filtered_df = df.copy()

# Apply Age Filters
if age_filter == "👶 0-1 Years (New)": filtered_df = filtered_df[(filtered_df['AGE_YEARS'] >= 0) & (filtered_df['AGE_YEARS'] <= 1.0)]
elif age_filter == "🚀 1-2 Years (Growing)": filtered_df = filtered_df[(filtered_df['AGE_YEARS'] > 1.0) & (filtered_df['AGE_YEARS'] <= 2.0)]
elif age_filter == "💼 2-5 Years (Experienced)": filtered_df = filtered_df[(filtered_df['AGE_YEARS'] > 2.0) & (filtered_df['AGE_YEARS'] <= 5.0)]
elif age_filter == "🏛️ 6-10 Years (Established)": filtered_df = filtered_df[(filtered_df['AGE_YEARS'] > 5.0) & (filtered_df['AGE_YEARS'] <= 10.0)]

# Apply Driver Filters
if driver_filter == "🚖 3 to 5 Drivers": filtered_df = filtered_df[(filtered_df['DRIVERS_COUNT'] >= 3) & (filtered_df['DRIVERS_COUNT'] <= 5)]
elif driver_filter == "👤 Exactly 1 Driver": filtered_df = filtered_df[filtered_df['DRIVERS_COUNT'] == 1]
elif driver_filter == "👥 Exactly 2 Drivers": filtered_df = filtered_df[filtered_df['DRIVERS_COUNT'] == 2]
elif driver_filter == "👥 Exactly 3 Drivers": filtered_df = filtered_df[filtered_df['DRIVERS_COUNT'] == 3]
elif driver_filter == "👥 Exactly 4 Drivers": filtered_df = filtered_df[filtered_df['DRIVERS_COUNT'] == 4]
elif driver_filter == "👥 Exactly 5 Drivers": filtered_df = filtered_df[filtered_df['DRIVERS_COUNT'] == 5]
elif driver_filter == "👥 6-10 Drivers": filtered_df = filtered_df[(filtered_df['DRIVERS_COUNT'] > 5) & (filtered_df['DRIVERS_COUNT'] <= 10)]
elif driver_filter == "🪪 11-50 Drivers": filtered_df = filtered_df[(filtered_df['DRIVERS_COUNT'] > 10) & (filtered_df['DRIVERS_COUNT'] <= 50)]

# Apply Zone Filter
if zone_filter != "🌐 All Zones":
    selected_zone = zone_filter.split()[-1] 
    if 'PHY_ZIP' in filtered_df.columns:
        filtered_df = filtered_df[filtered_df['PHY_ZIP'].astype(str).str.strip().str[0] == selected_zone]

# DYNAMIC STATE MULTISELECT FILTER
if 'PHY_STATE' in filtered_df.columns:
    available_states = sorted(filtered_df['PHY_STATE'].astype(str).str.strip().str.upper().unique().tolist())
    available_states = [s for s in available_states if s and s != 'NAN']
    
    if available_states:
        selected_states = st.sidebar.multiselect(
            "Select State(s) inside this Zone:",
            options=available_states,
            default=[],
            help="Leave empty to select ALL states inside this zone automatically."
        )
        if selected_states:
            filtered_df = filtered_df[filtered_df['PHY_STATE'].astype(str).str.strip().str.upper().isin(selected_states)]

# 🛡️ SMART FRAUD DETECTION TOGGLES
st.sidebar.markdown("---")
st.sidebar.subheader("🛡️ Fraud Prevention Toggles")

hide_po_box = st.sidebar.checkbox("🚫 Hide PO Box in Physical Address", value=False, help="Removes carriers using PO Boxes for physical addresses.")
only_prof_email = st.sidebar.checkbox("🌐 Only Show Professional Business Emails", value=False, help="Filters out generic emails like Gmail, Yahoo, Hotmail, etc.")
match_cities = st.sidebar.checkbox("🏠 Match Physical & Mailing City", value=False, help="Shows only carriers whose physical city matches their mailing city for maximum corporate transparency.")

# Apply PO Box Filter on PHY_STREET
if hide_po_box and 'PHY_STREET' in filtered_df.columns:
    po_pattern = r'\bP\.?\.?O\.?\s+BOX\b|POST\s+OFFICE\s+BOX'
    filtered_df = filtered_df[~filtered_df['PHY_STREET'].astype(str).str.contains(po_pattern, case=False, na=False, regex=True)]

# Apply Professional Email Filter
if only_prof_email and 'EMAIL_ADDRESS' in filtered_df.columns:
    free_domains = ['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com', 'aol.com', 'icloud.com']
    email_pattern = r'@(' + '|'.join([re.escape(d) for d in free_domains]) + r')$'
    filtered_df = filtered_df[~filtered_df['EMAIL_ADDRESS'].astype(str).str.strip().str.lower().str.contains(email_pattern, regex=True, na=False)]

# APPLY CITY MATCH LOGIC
if match_cities and 'PHY_CITY' in filtered_df.columns and 'CARRIER_MAILING_CITY' in filtered_df.columns:
    clean_phy_city = filtered_df['PHY_CITY'].astype(str).str.strip().str.upper()
    clean_mail_city = filtered_df['CARRIER_MAILING_CITY'].astype(str).str.strip().str.upper()
    filtered_df = filtered_df[clean_phy_city == clean_mail_city]

# ----------------------------------------------------------------------------------
# 🔍 2. INTERSECTION SEARCH
# ----------------------------------------------------------------------------------
st.markdown("### 🔍 Strict Batch Verification (Matches within Sidebar Filters)")
with st.container(border=True):
    col1, col2 = st.columns(2)
    
    with col1:
        search_type = st.radio("Search Mode 1:", ["Search Both (DOT/MC)", "USDOT Only", "MC Only"], horizontal=True)
        search_query = st.text_area(
            "1. Search by DOT / MC Number:",
            placeholder="Paste unlimited DOTs or MCs here...",
            height=120
        )
        
    with col2:
        st.radio("Search Mode 2:", ["Email & Phone Match"], horizontal=True, disabled=True)
        contact_query = st.text_area(
            "2. Search by Email or Phone Number (Mix allowed):",
            placeholder="Paste unlimited Emails or Phones from Loadboard...",
            height=120
        )

# Apply Search Filters
is_searching = False
search_mask = pd.Series(False, index=filtered_df.index)

if search_query.strip():
    is_searching = True
    raw_inputs = re.split(r'[\s,\n\r]+', search_query)
    cleaned_search_list = [item.upper().replace("MC", "").replace("DOT", "").replace("-", "").strip() for item in raw_inputs if item.strip()]
    
    if cleaned_search_list:
        dot_clean_series = filtered_df['DOT_NUMBER'].astype(str).str.strip()
        docket_clean_series = filtered_df['DOCKET1'].astype(str).str.upper().str.replace("MC", "").str.replace("-", "").str.strip()
        
        if search_type == "USDOT Only":
            search_mask = search_mask | dot_clean_series.isin(cleaned_search_list)
        elif search_type == "MC Only":
            search_mask = search_mask | docket_clean_series.isin(cleaned_search_list)
        else:
            search_mask = search_mask | dot_clean_series.isin(cleaned_search_list) | docket_clean_series.isin(cleaned_search_list)

if contact_query.strip():
    is_searching = True
    raw_contacts = re.split(r'[\s,\n\r]+', contact_query)
    clean_contacts = [c.strip().upper() for c in raw_contacts if c.strip()]
    
    if clean_contacts:
        search_phones = [re.sub(r'\D', '', c) for c in clean_contacts]
        search_phones = [p for p in search_phones if p] 
        
        df_emails = filtered_df['EMAIL_ADDRESS'].astype(str).str.strip().str.upper()
        df_phones = filtered_df['TELEPHONE'].astype(str).str.replace(r'\D', '', regex=True)
        
        cond_email = df_emails.isin(clean_contacts)
        cond_phone = df_phones.isin(search_phones)
        
        search_mask = search_mask | cond_email | cond_phone

if is_searching:
    filtered_df = filtered_df[search_mask]
    st.info("💡 Strict Search Active: Showing ONLY loadboard contacts that pass your Sidebar Filters.")

# Smart Decision Logic
def get_smart_decision(row):
    age = row.get('AGE_YEARS', 0)
    if pd.isna(age): return "⚪ Unknown"
    if age <= 1: return "🟢 New / Call Immediately"
    elif age <= 2: return "🟡 Growing / Good Target"
    elif age <= 5: return "🔵 Experienced / Reliable"
    else: return "🟣 Veteran / Established"
    
filtered_df['🛡️_DECISION'] = filtered_df.apply(get_smart_decision, axis=1)

if 'CARRIER_OPERATION' in filtered_df.columns:
    filtered_df['ROUTE_TYPE'] = filtered_df['CARRIER_OPERATION'].apply(
        lambda x: 'LONG-HAUL (INTERSTATE)' if str(x).strip().upper() == 'A' else 'LOCAL'
    )

st.success(f"📊 Found **{len(filtered_df):,}** highly targeted carriers matching all criteria.")

# DISPLAY COLUMNS SETUP
display_cols = [
    '🛡️_DECISION', 'STATUS_CODE', 'DOCKET1', 'DOT_NUMBER', 'LEGAL_NAME', 
    'TELEPHONE', 'EMAIL_ADDRESS', 'TOTAL_DRIVERS', 'MCS150_DATE', 
    'PHY_STREET', 'PHY_CITY', 'PHY_STATE', 'PHY_ZIP', 'PHY_COUNTRY',
    'CARRIER_MAILING_STREET', 'CARRIER_MAILING_CITY'
]
if 'ROUTE_TYPE' in filtered_df.columns: display_cols.append('ROUTE_TYPE')
display_cols = [col for col in display_cols if col in filtered_df.columns]

# ----------------------------------------------------------------------------------
# 📧 MULTI-STAGE AUTOMATED PIPELINE LOGISTICS GENERATOR
# ----------------------------------------------------------------------------------
st.markdown("### ✉️ Select Carriers to Generate Workflow Communications")

filtered_df.insert(0, "Select", False)
display_cols.insert(0, "Select")

edited_df = st.data_editor(
    filtered_df[display_cols],
    use_container_width=True,
    hide_index=True,
    column_config={"Select": st.column_config.CheckboxColumn("Select", default=False)},
    disabled=display_cols[1:] 
)

selected_carriers = edited_df[edited_df["Select"] == True]

if not selected_carriers.empty:
    st.markdown("---")
    st.markdown(f"### 🚀 Generated Pipeline Documents for {len(selected_carriers)} Carriers")
    
    selected_stage = st.selectbox(
        "📂 Select Communication Stage to View/Copy:",
        [
            "📞 Stage 0: Live Call Script & Audio Practice", # NEW ADDITION FOR AUDIO SCRIPT
            "1️⃣ Stage 1: Cold Outreach (Intro Email)", 
            "2️⃣ Stage 2: Lead Response (Document Request & Onboarding)", 
            "3️⃣ Stage 3: Official Dispatcher-Carrier Agreement (Flat 7%)",
            "4️⃣ Stage 4: Enterprise Identity Setup & Secured Load Board Access Matrix",
            "5️⃣ Stage 5: Carrier Packet Verification & Communication Systems Framework"
        ]
    )
    
    for index, row in selected_carriers.iterrows():
        legal_name = str(row.get('LEGAL_NAME', 'Carrier Team')).title()
        
        # --- FIXED EMAIL ADDRESS LOGIC ---
        raw_email = row.get('EMAIL_ADDRESS', '')
        if pd.isna(raw_email) or raw_email is None or str(raw_email).strip().upper() == 'NAN' or not str(raw_email).strip():
            email_address = 'No Email Provided'
        else:
            email_address = str(raw_email).strip().lower()
            
        dot_number = str(row.get('DOT_NUMBER', 'N/A'))
        docket_mc = str(row.get('DOCKET1', 'N/A')).upper().replace("MC", "").strip()
        
        # --- DYNAMIC VARIABLES ---
        phy_state = str(row.get('PHY_STATE', 'your state')).upper()
        total_drivers = str(row.get('TOTAL_DRIVERS', 'your'))
        domain_hint = legal_name.lower().replace(' ', '').replace(',', '').replace('.', '')
        
        with st.expander(f"📋 {selected_stage} Details for: {legal_name}", expanded=True):
            
            # ---------------------------------------------------------
            # 🎧 STAGE 0: LIVE CALL SCRIPT & AUDIO PRACTICE
            # ---------------------------------------------------------
            if "Stage 0" in selected_stage:
                st.markdown(f"### 📞 Live Dispatch Script for: **{legal_name}**")
                st.info("💡 **Tip:** Click the play button next to your lines to hear the correct pronunciation, then practice speaking.")
                
                # Dynamic Dialogue Array
                dialogue = [
                    {"role": "You", "text": f"Hi {legal_name}, this is Ahsan. Are you looking for extra freight support right now?"},
                    {"role": "Carrier", "text": "Not really, we're doing okay. Why are you calling?"},
                    {"role": "You", "text": "I understand. I work with private lanes that pay above average. Should I send my info?"},
                    {"role": "Carrier", "text": "Sure, send it over, I'll take a look."},
                    {"role": "You", "text": "Perfect, I'll email that now. I'll follow up in a few days. Thanks!"}
                ]
                
                for i, line in enumerate(dialogue):
                    col1, col2 = st.columns([0.85, 0.15])
                    
                    with col1:
                        box_class = "you-box" if line['role'] == "You" else "carrier-box"
                        st.markdown(f"""
                            <div class="chat-box {box_class}">
                                <b>{line['role']}:</b> {line['text']}
                            </div>
                        """, unsafe_allow_html=True)
                    
                    with col2:
                        if line['role'] == "You":
                            # Generate Audio (Google Text-to-Speech)
                            tts = gTTS(text=line['text'], lang='en', slow=False)
                            audio_buffer = io.BytesIO()
                            tts.write_to_fp(audio_buffer)
                            audio_buffer.seek(0)
                            st.audio(audio_buffer, format='audio/mp3')
                        else:
                            st.write("") # Empty space for Carrier side

            else:
                # ONLY SHOW EMAIL INFO FOR STAGES 1-5
                st.markdown("**Recipient Email Address:**")
                if email_address == 'No Email Provided':
                    st.error("No valid email address found for this carrier.")
                else:
                    st.code(email_address, language="text")
            
                # ---------------------------------------------------------
                # 🚀 STAGE 1: COLD OUTREACH
                # ---------------------------------------------------------
                if "Stage 1" in selected_stage:
                    subject_text = f"Maximizing Profit Margins for {legal_name} | DOT: {dot_number}"
                    body_text = f"""Hi {legal_name} Team,
    
We are a Freight Operations & Data Analytics team helping fleets in {phy_state} optimize their routes and maximize profit margins. We know you likely already have a dispatch setup, but we want to prove the power of our data-driven route planning for your team of {total_drivers} drivers.
    
Unlike traditional dispatchers who work on guesswork, our proprietary system synchronizes live EIA Diesel Indexes (GASDESW), USDA Capacity Scores, and BSL Historical Trend shifts every morning to isolate high-paying market loads before they drop.
    
We are offering to book 2 Test Loads completely free of charge. No 7% cuts, no hidden fees, and absolutely no contracts—just pure profit optimization to show you how our system out-negotiates brokers under your own MC Authority.
    
If our numbers beat your current setup, we can discuss working together long-term. Are you open to testing our free system for your trucks this week?
    
Best Regards,
Ahsan Khan
Operations & Data Analyst | System Intelligence Framework
https://sysintelofficial.com"""
    
                    st.markdown("**Subject Header:**")
                    st.code(subject_text, language="text")
                    st.markdown("**Email Body:**")
                    st.code(body_text, language="text")
                    
                    button_disabled = (email_address == 'No Email Provided')
                    if st.button(f"📧 Send Stage 1 Email to {legal_name}", key=f"send_s1_{dot_number}", disabled=button_disabled):
                        if "@" in email_address:
                            with st.spinner("Sending email via Zoho..."):
                                if send_direct_zoho_email(email_address, subject_text, body_text):
                                    st.success(f"✅ Email successfully sent to {email_address}!")
                                else:
                                    st.error("❌ Failed to send email. Please check your connection or password.")
                        else:
                            st.warning("⚠️ Invalid email format.")
                    
                # ---------------------------------------------------------
                # 🎯 STAGE 2: LEAD RESPONSE
                # ---------------------------------------------------------
                elif "Stage 2" in selected_stage:
                    subject_text = f"Trial Activation & Setup Requirements for {legal_name}"
                    body_text = f"""Hi {legal_name} Team,
    
Thank you for opting into our 2-Load Free Trial. We are excited to optimize the routes for your team of {total_drivers} drivers in {phy_state}.
    
To ensure a smooth process and secure the highest-paying loads directly under your MC Authority, we need your standard Carrier Setup Packet. Please reply to this email with:
    
1. Carrier Documents: W9, Active COI, MC Authority (COA), NOA, and Equipment specifics.
2. Load Board Access: For complete transparency and to avoid double-booking, please create a temporary Sub-User / Dispatcher login for us on your DAT or Truckstop account. We book everything directly under your name.
3. Professional Communication: Brokers prefer dealing directly with the carrier. Please provide a dispatcher email alias (e.g., dispatch@{domain_hint}.com) that we can use to officially represent your fleet.
    
Once we receive these, our analytics team will start hunting for your first premium load. Let's get to work!
    
Best Regards,
    
Ahsan Khan
Operations & Data Analyst | System Intelligence Framework
https://sysintelofficial.com"""
    
                    st.markdown("**Subject Header:**")
                    st.code(subject_text, language="text")
                    st.markdown("**Email Body:**")
                    st.code(body_text, language="text")
                    
                    button_disabled = (email_address == 'No Email Provided')
                    if st.button(f"📧 Send Stage 2 Email to {legal_name}", key=f"send_s2_{dot_number}", disabled=button_disabled):
                        if "@" in email_address:
                            with st.spinner("Sending email via Zoho..."):
                                if send_direct_zoho_email(email_address, subject_text, body_text):
                                    st.success(f"✅ Email successfully sent to {email_address}!")
                                else:
                                    st.error("❌ Failed to send email.")
                        else:
                            st.warning("⚠️ Invalid email format.")
                    
                # ---------------------------------------------------------
                # 📝 STAGE 3: AGREEMENT
                # ---------------------------------------------------------
                elif "Stage 3" in selected_stage:
                    current_date_str = datetime.now().strftime('%B %d, %Y')
                    
                    html_agreement_template = f"""
                    <div class="print-area" style="padding: 30px; font-family: Arial, sans-serif; max-width: 800px; margin: auto; background-color: #ffffff; color: #2D3748;">
                        <div style="border-bottom: 3px solid #2B6CB0; padding-bottom: 15px; margin-bottom: 30px; display: table; width: 100%;">
                            <div style="display: table-cell; font-size: 20pt; font-weight: bold; color: #1A365D;">SYSTEM INTELLIGENCE FRAMEWORK</div>
                            <div style="display: table-cell; text-align: right; font-size: 11pt; color: #4A5568; font-weight: bold; text-transform: uppercase; vertical-align: bottom;">Logistics Service Agreement</div>
                        </div>
                        <h2 style="text-align: center; font-size: 16pt; color: #1A365D; text-transform: uppercase; margin-bottom: 25px;">Independent Dispatcher-Carrier Service Agreement</h2>
                        <div style="background-color: #F7FAFC; border-left: 4px solid #2B6CB0; padding: 15px; margin-bottom: 25px; font-size: 10.5pt; text-align: justify;">
                            This Logistics Service Agreement (the "Agreement") is entered into and made effective as of this date of digital execution, by and between <strong>System Intelligence Framework</strong> (hereinafter referred to as "Dispatcher"), and <strong>{legal_name}</strong> operating under USDOT Number: <strong>{dot_number}</strong> / MC Number: <strong>{docket_mc}</strong> (hereinafter referred to as "Carrier").
                        </div>
                        <h3 style="font-size: 12pt; color: #2B6CB0; border-bottom: 1px solid #E2E8F0; padding-bottom: 5px; margin-top: 20px;">1. SCOPE OF MANAGEMENT SERVICES</h3>
                        <p style="font-size: 10pt; text-align: justify; margin-bottom: 10px;">Dispatcher agrees to provide independent commercial logistics management, including premium commercial freight sourcing utilizing active data analytics, broker background verification, complete execution of carrier setups, rate confirmations, comprehensive route optimization, and corporate back-office administrative handling.</p>
                        <h3 style="font-size: 12pt; color: #2B6CB0; border-bottom: 1px solid #E2E8F0; padding-bottom: 5px; margin-top: 20px;">2. CARRIER OBLIGATIONS & COMPLIANCE</h3>
                        <p style="font-size: 10pt; text-align: justify; margin-bottom: 10px;">Carrier retains full operational control and liability over its equipment and drivers. Carrier explicitly agrees to maintain an active FMCSA Interstate Operating Authority (COA), updated W-9, and active insurance coverage meeting absolute industry minimums at all times.</p>
                        <h3 style="font-size: 12pt; color: #2B6CB0; border-bottom: 1px solid #E2E8F0; padding-bottom: 5px; margin-top: 20px;">3. COMPENSATION & PAYMENT TERMS</h3>
                        <p style="font-size: 10pt; text-align: justify; margin-bottom: 10px;">In consideration for the services rendered, the Carrier agrees to pay Dispatcher a performance-based service fee of a <strong>flat 7% (Seven Percent)</strong> of the gross revenue of every individual load successfully sourced, confirmed, and executed through Dispatcher's framework.</p>
                        <h3 style="font-size: 12pt; color: #2B6CB0; border-bottom: 1px solid #E2E8F0; padding-bottom: 5px; margin-top: 20px;">4. TERM AND TERMINATION MATRIX</h3>
                        <p style="font-size: 10pt; text-align: justify; margin-bottom: 15px;">This agreement shall maintain a baseline active term of twelve (12) months. Either party maintains the absolute right to terminate this agreement at any time by delivering a <strong>three (3) day written notice</strong> of cancellation.</p>
                        <div style="margin-top: 50px; display: table; width: 100%;">
                            <div style="display: table-cell; width: 50%; padding-right: 20px; vertical-align: top;">
                                <div style="font-weight: bold; font-size: 10pt; color: #1A365D; margin-bottom: 35px;">FOR THE DISPATCHER:</div>
                                <div style="border-top: 1px solid #A0AEC0; width: 85%; margin-bottom: 5px;"></div>
                                <div style="font-size: 9.5pt; color: #4A5568;">Ahsan Khan | System Intelligence Framework</div>
                            </div>
                            <div style="display: table-cell; width: 50%; vertical-align: top;">
                                <div style="font-weight: bold; font-size: 10pt; color: #1A365D; margin-bottom: 35px;">FOR THE CARRIER (CLIENT):</div>
                                <div style="border-top: 1px solid #A0AEC0; width: 85%; margin-bottom: 5px;"></div>
                                <div style="font-size: 9.5pt; color: #4A5568;">Carrier Corporate Signatory Box</div>
                                <div style="font-size: 9pt; color: #718096;">Date of Digital Execution: {current_date_str}</div>
                            </div>
                        </div>
                    </div>
                    """
                    
                    st.markdown("**Live Executive Preview of Agreement:**")
                    st.components.v1.html(html_agreement_template, height=520, scrolling=True)
                    
                    print_js = f"""
                    <script>
                    function printAgreement() {{
                        var printWindow = window.open('', '_blank', 'width=900,height=800');
                        printWindow.document.write('<html><head><title>Dispatcher_Carrier_Agreement_{dot_number}</title>');
                        printWindow.document.write('</head><body style="margin:0; padding:0;">');
                        printWindow.document.write(`{html_agreement_template}`);
                        printWindow.document.write('</body></html>');
                        printWindow.document.close();
                        printWindow.focus();
                        setTimeout(function() {{ printWindow.print(); printWindow.close(); }}, 500);
                    }}
                    </script>
                    <button onclick="printAgreement()" style="background-color: #2B6CB0; color: white; padding: 12px 24px; border: none; border-radius: 6px; font-size: 11pt; font-weight: bold; cursor: pointer; width: 100%;">
                        🖨️ Open Print Engine / Save Agreement as Professional PDF
                    </button>
                    """
                    st.components.v1.html(print_js, height=70)
    
                # ---------------------------------------------------------
                # 🔑 STAGE 4: ENTERPRISE IDENTITY
                # ---------------------------------------------------------
                elif "Stage 4" in selected_stage:
                    st.markdown("<span class='badge-blue'>📡 Stage 4 Core Setup</span>", unsafe_allow_html=True)
                    
                    s4_subject = f"Urgent Operational Setup: Domain Email & Master Load Board Access Verification for {legal_name}"
                    s4_body = f"""Hi {legal_name} Team,
    
Our 7% Logistics Dispatch Agreement is now fully executed. To securely position your fleet on live premium load boards without risking third-party broker friction, we need to finalize your corporate email and system logins.
    
Please provide or initialize the following access layers immediately:
    
1. DEDICATED COMPANY EMAIL: A corporate domain extension (e.g., dispatch@{domain_hint}.com) OR a dedicated professional gmail account managed strictly for bookings.
2. DAT POWER/ONE LOAD BOARD: Master or sub-user portal credentials (Username & Password) so we can negotiate freight directly under your MC.
3. TRUCKSTOP INFRASTRUCTURE: Active login keys for lane bidding.
    
Broker systems verify matching email footprints for fraud safety; using these direct setups ensures 100% confirmation speed. Reply to this line with your finalized credentials list below.
    
Best Regards,
Ahsan Khan | System Intelligence Framework"""
    
                    st.markdown("**1. Outbound Access Request Email:**")
                    st.text_input("📋 Subject Header:", value=s4_subject, key=f"s4_sub_{dot_number}")
                    st.text_area("📝 Message Body Content:", value=s4_body, height=280, key=f"s4_body_{dot_number}")
                    
                    button_disabled = (email_address == 'No Email Provided')
                    if st.button(f"📧 Send Stage 4 Email to {legal_name}", key=f"send_s4_{dot_number}", disabled=button_disabled):
                        if "@" in email_address:
                            with st.spinner("Sending email via Zoho..."):
                                if send_direct_zoho_email(email_address, s4_subject, s4_body):
                                    st.success(f"✅ Email successfully sent to {email_address}!")
                                else:
                                    st.error("❌ Failed to send email.")
                        else:
                            st.warning("⚠️ Invalid email format.")
                    
                    st.markdown("---")
                    st.markdown("**2. 🔒 Session Ingestion Matrix (Secure Data Entry):**")
                    
                    sc1, sc2 = st.columns(2)
                    with sc1:
                        logged_email = st.text_input("✉️ Integrated Carrier Domain Email:", placeholder="dispatch@carrier.com", key=f"ins_em_{dot_number}")
                        dat_user = st.text_input("👤 DAT User ID:", placeholder="DAT Username", key=f"ins_du_{dot_number}")
                        dat_pass = st.text_input("🔒 DAT Password Key:", type="password", placeholder="DAT Password", key=f"ins_dp_{dot_number}")
                    with sc2:
                        ts_user = st.text_input("💎 Truckstop User ID:", placeholder="Truckstop Username", key=f"ins_tu_{dot_number}")
                        ts_pass = st.text_input("🔒 Truckstop Password Key:", type="password", placeholder="Truckstop Password", key=f"ins_tp_{dot_number}")
                    
                    if st.checkbox("🔓 Reveal Session Keycodes for Verification", key=f"rev_box_{dot_number}"):
                        st.warning(f"DAT Pass: `{dat_pass}` | Truckstop Pass: `{ts_pass}`")
                        
                # ---------------------------------------------------------
                # 📁 STAGE 5: VERIFICATION
                # ---------------------------------------------------------
                elif "Stage 5" in selected_stage:
                    st.markdown("<span class='badge-green'>🚀 Stage 5 Full Activation</span>", unsafe_allow_html=True)
                    
                    st.markdown("**1. Secure Carrier Packet Vault Checklist:**")
                    dc1, dc2, dc3, dc4 = st.columns(4)
                    with dc1: mc_chk = st.checkbox("MC Authority Letter", value=True, key=f"chk_mc_{dot_number}")
                    with dc2: coi_chk = st.checkbox("COI Insurance Approved", value=True, key=f"chk_coi_{dot_number}")
                    with dc3: w9_chk = st.checkbox("IRS W-9 Form Saved", value=True, key=f"chk_w9_{dot_number}")
                    with dc4: noa_chk = st.checkbox("Factoring NOA Archived", value=False, key=f"chk_noa_{dot_number}")
                    
                    st.markdown("---")
                    st.markdown("**2. Communications Grid & Future Google Voice Roadmap:**")
                    cc1, cc2 = st.columns(2)
                    with cc1:
                        active_voip = st.selectbox(
                            "📞 Current Active VOIP System Line:",
                            ["Active (Zadarma System Lines)", "Active (OpenPhone Network)", "Active (Other Extension Provider)", "Pending Ingestion"],
                            index=0, key=f"voip_sel_{dot_number}"
                        )
                    with cc2:
                        migration_target = st.date_input(
                            "⏳ Planned Google Voice Premium Shift Date:",
                            value=datetime.now().date() + timedelta(days=90),
                            key=f"gv_date_{dot_number}"
                        )
                    
                    days_remaining = (migration_target - datetime.now().date()).days
                    st.markdown("<div class='secure-card'>", unsafe_allow_html=True)
                    if days_remaining > 0:
                        st.info(f"⏳ **Fleet Scaling Growth Radar:** Your system is operating safely on your temporary VOIP pipeline. You have **{days_remaining} days** left before switching this fleet to the premium **Google Voice Ecosystem** ({migration_target.strftime('%m/%d/%Y')}).")
                    else:
                        st.error("🚨 **System Alert Requirement:** The 90-day stabilization cycle is mature! Move this carrier from current VOIP lines to **Google Voice** immediately for native dialing validation.")
                    st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------------------------------------------------------------
# Export Section
st.sidebar.markdown("---")
st.sidebar.markdown("### 💾 Export Leads")

@st.cache_data
def convert_df_to_csv(df_to_convert):
    export_df = df_to_convert.drop(columns=['Select'], errors='ignore')
    return export_df.to_csv(index=False).encode('utf-8')

csv_bytes = convert_df_to_csv(filtered_df[display_cols])

st.sidebar.download_button(
    label="📥 Download as CSV",
    data=csv_bytes,
    file_name=f"fmcsa_filtered_leads_{datetime.now().strftime('%Y%m%d')}.csv",
    mime="text/csv"
)
