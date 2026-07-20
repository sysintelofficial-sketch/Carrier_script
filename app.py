import streamlit as st
import asyncio
import edge_tts
import io

# 1. Page Setup - "wide" layout for full screen spread
st.set_page_config(page_title="Carrier Pitch Trainer", layout="wide")

# 2. Custom CSS for 100% Zoom and Large Fonts
st.markdown("""
    <style>
    /* Font size increase (22px) for clear readability */
    .chat-box { 
        padding: 20px; 
        border-radius: 12px; 
        font-size: 22px !important; 
        line-height: 1.6;
        margin-bottom: 15px;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
    }
    /* Distinct colors for You and Carrier */
    .you-box { background-color: #e3f2fd; color: #0d47a1; border-left: 8px solid #1976d2; }
    .carrier-box { background-color: #ffebee; color: #b71c1c; border-left: 8px solid #d32f2f; }
    </style>
""", unsafe_allow_html=True)

# 3. Header Section
st.title("📞 Live Call Script & Audio Practice (Male Voice)")
st.info("💡 मेल (Male) अमेरिकन वॉइस में सुनने और प्रैक्टिस करने के लिए प्ले (Play) बटन पर क्लिक करें।")

# Async function to generate male voice using Edge TTS
async def generate_male_audio(text):
    # 'en-US-GuyNeural' is a high-quality American Male Voice
    communicate = edge_tts.Communicate(text, "en-US-GuyNeural")
    audio_data = bytearray()
    async for chunk in communicate.stream():
        if chunk["type"] == "audio":
            audio_data.extend(chunk["data"])
    return bytes(audio_data)

# 4. Your Dialogue Script Array
dialogue = [
    {"role": "You", "text": "Hi, am I speaking with the owner or dispatch? This is Ahsan. Are you looking for extra freight support right now?"},
    {"role": "Carrier", "text": "Not really, we're doing okay. Why are you calling?"},
    {"role": "You", "text": "I completely understand. I work with private lanes that pay above average in your area. Should I send my info so you have it as a backup?"},
    {"role": "Carrier", "text": "Sure, send it over, I'll take a look."},
    {"role": "You", "text": "Perfect, I'll email that right now. Have a great day and stay safe out there!"}
]

# 5. Display Loop
for line in dialogue:
    # Creating a wide layout with columns (Text on left, Audio on right)
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
            # Generate Audio for Your lines only
            audio_bytes = asyncio.run(generate_male_audio(line['text']))
            
            # Simple margin tweak to align the audio player vertically with the big text boxes
            st.write("<br>", unsafe_allow_html=True) 
            st.audio(audio_bytes, format='audio/mp3')
        else:
            st.write("") # Empty space for Carrier side
