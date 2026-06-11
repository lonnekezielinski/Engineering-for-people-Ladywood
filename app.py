import streamlit as st
import base64
from translations import t, apply_rtl_css

# PAGE CONFIG
st.set_page_config(page_title="Ladywood Connect", layout="wide")

# Load logo
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

logo_icon = get_base64_image("assets/waypoint-logo.png")

# Language settings
LANGUAGE_OPTIONS = [
    "🇬🇧 English",
    "🇸🇦 Arabic",
    "🇵🇰 Urdu",
    "🇵🇰 Punjabi",
    "🇧🇩 Bengali",
    "🇧🇩 Bengali (Sylheti)",
    "🇧🇩 Bengali (Chatgaya)",
    "🇵🇱 Polish",
]
LANGUAGE_MAP = {
    "🇬🇧 English":           "English",
    "🇸🇦 Arabic":             "Arabic",
    "🇵🇰 Urdu":               "Urdu",
    "🇵🇰 Punjabi":            "Punjabi",
    "🇧🇩 Bengali":            "Bengali",
    "🇧🇩 Bengali (Sylheti)":  "Sylheti",
    "🇧🇩 Bengali (Chatgaya)": "Chatgaya",
    "🇵🇱 Polish":             "Polish",
}

if "language" not in st.session_state:
    if "lang" in st.query_params:
        url_lang = st.query_params["lang"]
        if url_lang in ["English","Arabic","Urdu","Punjabi","Bengali","Sylheti","Chatgaya","Polish"]:
            st.session_state["language"] = url_lang
        else:
            st.session_state["language"] = "English"
    else:
        st.session_state["language"] = "English"

lang = st.session_state["language"]

# Text sizing
if "text_size" in st.query_params:
    url_text_size = st.query_params["text_size"]
    if url_text_size in ["S", "M", "L"]:
        st.session_state["text_size"] = url_text_size

if "text_size" not in st.session_state:
    st.session_state["text_size"] = "S"

text_size = st.session_state["text_size"]

if text_size == "S":
    title_size = "72px"
    subtitle_size = "24px"
    card_title_size = "30px"
    setting_label_size = "18px"

    mobile_title_size = "38px"
    mobile_subtitle_size = "18px"
    mobile_card_title_size = "22px"

elif text_size == "M":
    title_size = "84px"
    subtitle_size = "28px"
    card_title_size = "36px"
    setting_label_size = "22px"

    mobile_title_size = "44px"
    mobile_subtitle_size = "21px"
    mobile_card_title_size = "26px"

elif text_size == "L":
    title_size = "96px"
    subtitle_size = "32px"
    card_title_size = "42px"
    setting_label_size = "26px"

    mobile_title_size = "50px"
    mobile_subtitle_size = "24px"
    mobile_card_title_size = "30px"

# CUSTOM CSS
st.markdown(f"""
<style>
/* --- Page layout --- */ 
[data-testid="stAppViewContainer"] {{ background-color: #F5F2EA; }}
[data-testid="stHeader"]           {{ background-color: transparent; }}
[data-testid="stToolbar"]          {{ right: 2rem; }}
[data-testid="stSidebar"]          {{ display: none; }}
.block-container                   {{ padding: 2rem 3rem; }}

/* --- Header title and logo --- */
.title      {{ font-size: {title_size}; font-weight: 800; color: #0D1B3D; }}
.subtitle   {{ font-size: {subtitle_size}; font-weight: 500; color: #444; margin-bottom: 40px; }}
.title-row  {{ display: flex; align-items: center; gap: 20px; }}
.title-logo {{ width: 90px; height: 90px; object-fit: contain; }}

/* --- Date and weather box --- */ 
.weather-box {{
    background: #FAFAFA; border: 2px solid #D8D2C7; border-radius: 18px;
    padding: 22px; display: flex; justify-content: space-between;
    color: #1A1A1A; font-size: 20px; font-weight: 500;
}}

/* --- Homepage cards --- */
.card {{
    height: 240px; padding: 30px; border-radius: 32px;
    border: 2px solid rgba(0,0,0,0.05);
    display: flex; flex-direction: column;
    justify-content: center; align-items: center; gap: 18px;
    margin-bottom: 25px; cursor: pointer; transition: 0.2s;
}}
.card:hover     {{ transform: scale(1.02); }}
.card-icon      {{ font-size: 80px; line-height: 1;}}
.card-title     {{ font-size: {card_title_size}; font-weight: 800; margin-top: 8px; }}

/* Card background colors */
.bus           {{ background-color: #DDB8E8; }}
.workshops     {{ background-color: #C8E2F5; }}
.announcements {{ background-color: #CFEAC2; }}
.feedback      {{ background-color: #F4D2BD; }}

/* Card title colors */
.bus .card-title           {{ color: #5A2E75; }}
.workshops .card-title     {{ color: #285C7A; }}
.announcements .card-title {{ color: #3D6B32; }}
.feedback .card-title      {{ color: #9A5B2E; }}

/* Removes default link style around card */
a {{ text-decoration: none !important; color: inherit !important; }}

/* --- Accessibility settings --- */
.setting-label {{ font-size: {setting_label_size}; font-weight: 600; color: #0D1B3D; margin-bottom: 8px; }}

/* Language dropdown menu */
[data-testid="stSelectbox"] {{ width: 320px !important; max-width: 320px; margin-top: 0; }}
[data-testid="stSelectbox"] label {{ display: none; }}
[data-baseweb="select"] > div {{ background-color: white !important; border: 2px solid #D8D2C7 !important; border-radius: 18px !important; color: #222 !important; }}
[data-baseweb="select"] span  {{ color: #222 !important; font-weight: 500; }}

/* Text size radio buttons */
[data-testid="stRadio"] {{
    width: 220px !important; background: white; border: 2px solid #D8D2C7;
    border-radius: 18px; padding: 8px 12px; margin-top: 0; margin-left: 0 !important;
}}
div[role="radiogroup"] label p {{ color: #0D1B3D !important; font-weight: 600 !important; font-size: 16px !important; }}

/* --- Mobile layout fixes --- */
@media (max-width: 768px) {{
    html, body, [data-testid="stAppViewContainer"] {{ overflow-x: hidden !important; }}
    .block-container {{ padding-left: 1rem !important; padding-right: 1rem !important; padding-top: 1rem !important; max-width: 100% !important; }}

    /* General page titles */
    .title, .page-title {{ font-size: 38px !important; line-height: 1.1 !important; word-break: normal !important; overflow-wrap: normal !important; }}

    /* Break headings correctly */
    h1, h2, h3 {{ word-break: normal !important; overflow-wrap: normal !important; }}

    /* Subtitle */
    .subtitle {{ font-size: 18px !important; }}

    /* Homepage cards */
    .card {{ height: 165px !important; padding: 18px !important; border-radius: 24px !important; margin-bottom: 18px !important; }}
    .card-icon {{ font-size: 55px; }}
    .card-title {{ font-size: {mobile_card_title_size} !important; text-align: center !important; line-height: 1.2 !important; }}

    /* Accessibility controls */
    [data-testid="stSelectbox"], [data-testid="stRadio"] {{ width: 100% !important; max-width: 100% !important; }}

    /* Back button */
    .stButton > button {{ font-size: 16px !important; padding: 10px 14px !important; margin-bottom: 20px !important; }}
      
    /* Weather and date */
    .weather-box {{ margin-bottom: 25px !important; font-size: 15px !important; padding: 14px !important; flex-direction: column !important; gap: 8px !important; }}
}}
</style>
""", unsafe_allow_html=True)

# Right-to-left layout for certain languages
st.markdown(apply_rtl_css(lang), unsafe_allow_html=True)

# --- Header ---
col1, col2 = st.columns([4, 1])
with col1:
    st.markdown(f"""
    <div class="title-row">
        <img class="title-logo"
            src="data:image/png;base64,{logo_icon}">
        <div class="title">{t("app_title", lang)}</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown(f'<div class="subtitle">{t("app_subtitle", lang)}</div>', unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class='weather-box'>
        <span>📅 19 June 2026</span>
        <span>⛅ 17°C</span>
    </div>
    """, unsafe_allow_html=True)


# --- Card grid ---
col1, col2 = st.columns(2)
with col1:
    st.markdown(f"""
    <a href="bus?lang={lang}&text_size={st.session_state["text_size"]}" target="_self">
        <div class='card bus'>
            <div class='card-icon'>🚌</div>
            <div class='card-title'>{t("nav_bus", lang)}</div>
        </div>
    </a>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <a href="announcements?lang={lang}&text_size={st.session_state["text_size"]}" target="_self">
        <div class='card announcements'>
            <div class='card-icon'>📢</div>
            <div class='card-title'>{t("nav_announcements", lang)}</div>
        </div>
    </a>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <a href="workshops?lang={lang}&text_size={st.session_state["text_size"]}" target="_self">
        <div class='card workshops'>
            <div class='card-icon'>💻</div>
            <div class='card-title'>{t("nav_workshops", lang)}</div>
        </div>
    </a>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <a href="feedback?lang={lang}&text_size={st.session_state["text_size"]}" target="_self">
        <div class='card feedback'>
            <div class='card-icon'>📋</div>
            <div class='card-title'>{t("nav_feedback", lang)}</div>
        </div>
    </a>
    """, unsafe_allow_html=True)

# --- Bottom settings ---
bottom1, bottom2 = st.columns([1, 1])
with bottom1:
    st.markdown(f"<div class='setting-label'>{t('label_language', lang)}</div>", unsafe_allow_html=True)
    selected_display = st.selectbox(
        "Language",
        LANGUAGE_OPTIONS,
        index=LANGUAGE_OPTIONS.index(next(k for k, v in LANGUAGE_MAP.items() if v == lang)),
        label_visibility="collapsed"
    )
    # Update session state when language changes → triggers rerun
    new_lang = LANGUAGE_MAP[selected_display]
    if new_lang != st.session_state["language"]:
        st.session_state["language"] = new_lang
        st.query_params["lang"] = new_lang
        st.rerun()

with bottom2:
    st.markdown(f"<div class='setting-label'>{t('label_textsize', lang)}</div>", unsafe_allow_html=True)

    text_size_choice = st.radio(
        "Text size",
        ["S", "M", "L"],
        index=["S", "M", "L"].index(st.session_state["text_size"]),
        horizontal=True,
        label_visibility="collapsed",
        key="home_text_size_radio"
    )

    if text_size_choice != st.session_state["text_size"]:
        st.session_state["text_size"] = text_size_choice
        st.query_params["text_size"] = text_size_choice
        st.rerun()