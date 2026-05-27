# This is the code for the homepage of the application, to change any other page go to their corresponding file in the "page”

# To run: open terminal -> activate virtual environment: venv/Scripts/activate (Windows) or source venv/bin/activate (Mac) -> streamlit run app.py in terminal
# To stop the application: ctrl + C in terminal (or cmd + C)

# IMPORTS 
import streamlit as st
from PIL import Image #If we want to make a logo keep this library
import base64

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

bus_icon = get_base64_image("assets/front-of-bus.png")
workshop_icon = get_base64_image("assets/calendar.png")
announcement_icon = get_base64_image("assets/megaphone.png")
feedback_icon = get_base64_image("assets/chat.png")

# PAGE CONFIG
st.set_page_config(
    page_title="Ladywood Connect",
    layout="wide"
)

### CUSTOM CSS
st.markdown("""
<style>
            
/* ---app background and streamlit overrides--- */
[data-testid="stAppViewContainer"] {
    background-color: #F5F2EA;
}

[data-testid="stHeader"] {
    background-color: transparent;
}

[data-testid="stToolbar"] {
    right: 2rem;
}

[data-testid="stSidebar"] {
    display:none;
}

/* ---page spacing--- */         
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* ---header styling: titles and subtitles--- */
.title {
    font-size: 72px;
    font-weight: 800;
    color: #0D1B3D;
}

.subtitle {
    font-size: 24px;
    color: #444;
    margin-bottom: 40px;
}

/* ---main cards and their styling--- */
.card {
    border-radius: 32px;
    padding: 50px;
    height: 260px;
    display:flex;
    flex-direction:column;
    justify-content:center;
    align-items:center;
    margin-bottom:35px;
    border:2px solid;
    cursor:pointer;
    transition:0.2s;
}

.card img {
    width:110px;
}

.card-title {
    font-size:30px;
    font-weight:700;
    margin-top:25px;
}

.card:hover {
    transform: scale(1.02);
}

/* card colors */
.bus {
    background-color: #DDB8E8;
}

.workshops {
    background-color: #C8E2F5;
}

.announcements {
    background-color: #CFEAC2;
}

.feedback {
    background-color: #F4D2BD;
}
            
/* ---weather and date boxes in top right corner--- */           
.weather-box{
    background:#FAFAFA;
    border:2px solid #D8D2C7;
    border-radius:18px;
    padding:22px;
    display:flex;
    justify-content:space-between;
    color:#1A1A1A;
    font-size:20px;
    font-weight:500;
}

/* ---accessibility controls--- */
.text-size-box{
    background:white;
    border:2px solid #D8D2C7;
    border-radius:18px;
    padding:18px 28px;
    display:flex;
    align-items:center;
    gap:20px;
    width:fit-content;
    margin-left:auto;
    color:#222;
}

.smallA{
    font-size:18px;
}

.medA{
    font-size:26px;
}

.bigA{
    font-size:38px;
}

/* ---link styling: it removes the default hyperlink formatting for clickable card in streamlit--- */           
a {
    text-decoration:none !important;
    color:inherit !important;
}
/* ---language dropdown styling--- */
[data-testid="stSelectbox"] label {
    font-size: 20px;
    font-weight: 600;
    color: #0D1B3D;
}

[data-testid="stSelectbox"] > div > div {
    background: white;
    border: 2px solid #D8D2C7 !important;
    border-radius: 18px !important;
    padding: 12px 28px;
    font-size: 18px;
    font-weight: 500;
    color: #222;
}

/* ---text size radio styling--- */
[data-testid = "stRadio"] {
    background: white;
    border: 2px solid #D8D2C7;
    border-radius: 18px;
    padding: 18px 28px;
}

[data-testid = "stRadio"] label{
    font-weight: 700;
    color: #0D1B3D;
}

[data-testid="stRadio"] >div > label:nth-child(1) span:last-child { font-size: 16px; }
[data-testid="stRadio"] >div > label:nth-child(2) span:last-child { font-size : 22px'; }
[data-testid="stRadio"] >div > label:nth-child(3) span:last-child{ font-size: 30px; }
</style>
""", unsafe_allow_html=True)

### HEADER
col1, col2 = st.columns([4,1])

with col1:
    st.markdown(
        '<div class="title">Ladywood Connect</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Your community hub</div>',
        unsafe_allow_html=True
    )

with col2:
    st.markdown("""
    <div class='weather-box'>
        <span>📅 27 May 2026</span>
        <span>☀️ 25°C</span>
    </div>
    """, unsafe_allow_html=True)
# We now have to set the temp and date, we could try to make it so that it becomes automatic. However i do think that for the prototype this is fine.

### BUTTON GRID
col1, col2 = st.columns(2)

with col1:

    st.page_link(
        "pages/bus.py",
        label="",
        icon=None
    )

    st.markdown(f"""
    <a href="bus" target="_self">
        <div class='card bus'>
            <img src='data:image/png;base64,{bus_icon}'>
            <div class='card-title'>Bus</div>
        </div>
    </a>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <a href="announcements" target="_self">
        <div class='card announcements'>
            <img src='data:image/png;base64,{announcement_icon}'>
            <div class='card-title'>Announcements</div>
        </div>
    </a>
    """, unsafe_allow_html=True)

with col2:

    st.markdown(f"""
    <a href="workshops" target="_self">
        <div class='card workshops'>
            <img src='data:image/png;base64,{workshop_icon}'>
            <div class='card-title'>Workshops</div>
        </div>
    </a>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <a href="feedback" target="_self">
        <div class='card feedback'>
            <img src='data:image/png;base64,{feedback_icon}'>
            <div class='card-title'>Feedback & Requests</div>
        </div>
    </a>
    """, unsafe_allow_html=True)

# BOTTOM SETTINGS
bottom1, bottom2 = st.columns([1,1])

with bottom1:
    st.markdown("<div style='background:white; border:2px solid #D8D2C7: border-radius:18px; padding:18px 28px;'>", unsafe_allow_html=True)

    language = st.selectbox(
        "🌐 Language",
        ["🇬🇧 English", "🇸🇦 Arabic", "🇵🇰 Urdu", "🇵🇰 Punjabi"],
        label_visibility="visible"
    )
    st.markdown("</div>", unsafe_allow_html=True)
    # Change languages based on the most spoken languages in Ladywood


with bottom2: 
    st.markdown("""
    <div class='text-size-box'>
        Text size
        <span class='smallA'>A</span>
        <span class='medA'>A</span>
        <span class='bigA'>A</span>
    </div>
    """, unsafe_allow_html=True)
    text_size = st.radio(
        "Text size", ["A", "A+", "A++"], 
        horizontal= True,
        label_visibility = "visible"
    )
# We need to change the appearance and the functions of the bottom settings:
# - make the text size function look like you can actually click on it, so like the commented code above
# - make language dropdown menu look more aesthetically pleasing or at least make both bottom settings look the same

# Extra to do:
# - make a logo and add it?
# - make the design for the pages (bus, announcements, feedback, workshops)
# - make sure the icon of the pages is in front of the title so "🚌 Bus" but with the png image