# To run: open terminal -> activate virtual environment: venv/Scripts/activate (Windows) or source venv/bin/activate (Mac) -> streamlit run app.py in terminal
# To stop the application: ctrl + C in terminal (or cmd + C)

# IMPORTS 
import streamlit as st
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
/* ---APP BACKGROUND + STREAMLIT OVERRIDES--- */

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
    display: none;
}

.block-container {
    padding: 2rem 3rem;
}

/* ---HEADER--- */

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

.weather-box {
    background: #FAFAFA;
    border: 2px solid #D8D2C7;
    border-radius: 18px;
    padding: 22px;

    display: flex;
    justify-content: space-between;

    color: #1A1A1A;
    font-size: 20px;
    font-weight: 500;
}


/* ---MAIN NAVIGATION CARDS--- */
.card {
    height: 240px;
    padding: 30px;

    border-radius: 32px;
    border: 2px solid rgba(0,0,0,0.05);

    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 18px;

    margin-bottom: 25px;

    cursor: pointer;
    transition: 0.2s;
}

.card:hover {
    transform: scale(1.02);
}

.card img {
    width: 85px;
    height: 85px;
    object-fit: contain;
}

.card-title {
    font-size: 30px;
    font-weight: 800;
    margin-top: 8px;
}

/* Card background colours */

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

/* Card icon colours */
.bus img {
    filter: brightness(0) saturate(100%) invert(18%) sepia(17%) saturate(1170%) hue-rotate(246deg) brightness(92%) contrast(90%);
}

.workshops img {
    filter: brightness(0) saturate(100%) invert(29%) sepia(18%) saturate(926%) hue-rotate(172deg) brightness(92%) contrast(90%);
}

.announcements img {
    filter: brightness(0) saturate(100%) invert(31%) sepia(15%) saturate(1118%) hue-rotate(64deg) brightness(92%) contrast(90%);
}

.feedback img {
    filter: brightness(0) saturate(100%) invert(32%) sepia(34%) saturate(643%) hue-rotate(340deg) brightness(92%) contrast(90%);
}

/* Card title colours */
.bus .card-title {
    color: #5A2E75;
}

.workshops .card-title {
    color: #285C7A;
}

.announcements .card-title {
    color: #3D6B32;
}

.feedback .card-title {
    color: #9A5B2E;
}

/* ---LINKS: Removes default hyperlink styling from cards--- */
a {
    text-decoration: none !important;
    color: inherit !important;
}

/* ---BOTTOM SETTINGS: Language + text size controls--- */
.setting-label {
    font-size: 18px;
    font-weight: 600;
    color: #0D1B3D;
    margin-bottom: 8px;
}

/* Language dropdown */
[data-testid="stSelectbox"] {
    width: 320px !important;
    max-width: 320px;
    margin-top: 0;
}

[data-testid="stSelectbox"] label {
    display: none;
}

[data-baseweb="select"] > div {
    background-color: white !important;
    border: 2px solid #D8D2C7 !important;
    border-radius: 18px !important;
    color: #222 !important;
}

[data-baseweb="select"] span {
    color: #222 !important;
    font-weight: 500;
}

/* Text size selector */
[data-testid="stRadio"] {
    width: 220px !important;
    background: white;
    border: 2px solid #D8D2C7;
    border-radius: 18px;
    padding: 8px 12px;
    margin-top: 0;
    margin-left: 0 !important;
}

div[role="radiogroup"] label p {
    color: #0D1B3D !important;
    font-weight: 600 !important;
    font-size: 16px !important;
}
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
        <span>📅 28 May 2026</span>
        <span>☀️ 25°C</span>
    </div>
    """, unsafe_allow_html=True)
# We now have to set the temp and date, we could try to make it so that it becomes automatic. However i do think that for the prototype this is fine.

### BUTTON GRID
col1, col2 = st.columns(2)

with col1:
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
bottom1, bottom2 = st.columns([1, 1])

with bottom1:
    st.markdown(
    "<div class='setting-label'>🌐 Language</div>",
    unsafe_allow_html=True
)

    language = st.selectbox(
        "",
        [
            "🇬🇧 English",
            "🇸🇦 Arabic",
            "🇵🇰 Urdu",
            "🇵🇰 Punjabi"
        ],
        label_visibility="collapsed"
    )

with bottom2:
    st.markdown(
        "<div class='setting-label'>🔠 Text size</div>",
        unsafe_allow_html=True
    )

    text_size = st.radio(
        "",
        ["A", "A+", "A++"],
        horizontal=True,
        label_visibility="collapsed"
    )

# We need to change the appearance and the functions of the bottom settings:
# - make the text size function look like you can actually click on it, so like the commented code above
# - make language dropdown menu look more aesthetically pleasing or at least make both bottom settings look the same

# Extra to do:
# - make a logo and add it?
# - make the design for the pages (bus, announcements, feedback, workshops)
# - make sure the icon of the pages is in front of the title so "🚌 Bus" but with the png image