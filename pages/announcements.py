### IMPORTS
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import streamlit as st
import base64
from translations import t, apply_rtl_css

### PAGE CONFIG
st.set_page_config(page_title="Announcements", layout="wide")

# Read language from URL or session state
if "language" not in st.session_state:
    if "lang" in st.query_params:
        url_lang = st.query_params["lang"]
        if url_lang in ["English","Arabic","Urdu","Punjabi","Bengali","Sylheti","Chatgaya","Polish"]:
            st.session_state["language"] = url_lang
        else:
            st.session_state["language"] = "English"
    else:
        st.session_state["language"] = "English"

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

lang = st.session_state.get("language", "English")

if "text_size" in st.query_params:
    url_text_size = st.query_params["text_size"]
    if url_text_size in ["S", "M", "L"]:
        st.session_state["text_size"] = url_text_size

if "text_size" not in st.session_state:
    st.session_state["text_size"] = "S"

text_size = st.session_state["text_size"]

if text_size == "S":
    page_title_size = "58px"
    body_size = "18px"
    card_title_size = "28px"
    button_size = "20px"

    mobile_page_title_size = "40px"
    mobile_body_size = "16px"
    mobile_card_title_size = "22px"
    mobile_button_size = "18px"

elif text_size == "M":
    page_title_size = "70px"
    body_size = "22px"
    card_title_size = "34px"
    button_size = "24px"

    mobile_page_title_size = "46px"
    mobile_body_size = "19px"
    mobile_card_title_size = "26px"
    mobile_button_size = "21px"

elif text_size == "L":
    page_title_size = "82px"
    body_size = "26px"
    card_title_size = "40px"
    button_size = "28px"

    mobile_page_title_size = "52px"
    mobile_body_size = "22px"
    mobile_card_title_size = "30px"
    mobile_button_size = "24px"

### FUNCTION FOR PNG ICON
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

announcement_icon = get_base64_image("assets/megaphone.png")

### CUSTOM CSS
st.markdown(f"""
<style>
[data-testid="stAppViewContainer"] {{ background-color: #F5F2EA; }}
[data-testid="stHeader"]           {{ background: transparent; }}
[data-testid="stToolbar"]          {{ right: 2rem; }}
[data-testid="stSidebar"]          {{ display: none; }}
.block-container {{ max-width:none; width:100%; padding-top:2rem; padding-bottom:2rem; padding-left:4rem; padding-right:4rem; }}

.stButton > button {{ background:white; border-radius:18px; border:2px solid #D8D2C7; padding:12px 18px; font-size:18px; color:#444; margin-bottom:25px; }}

.page-title    {{ font-size:{page_title_size}; font-weight:900; color:#0D1B3D; margin-bottom:5px; }}
.page-subtitle {{ font-size:20px; color:#555; margin-bottom:30px; }}

.subtitle-box {{ background:#CFEAC2; border:2px solid #A8D8A0; border-radius:24px; padding:20px 28px; margin-bottom:30px; font-size:{body_size}; color:#1A3E1A; }}

.announcement-card {{ background:white; border-radius:28px; padding:22px; margin-bottom:22px; display:flex; flex-direction:row; align-items:center; gap:24px; border:2px solid rgba(0,0,0,0.05); box-shadow:0 4px 12px rgba(0,0,0,0.04); transition:0.2s; }}
.announcement-card:hover {{ transform:scale(1.01); }}
.icon-box {{ width:110px; height:110px; border-radius:25px; display:flex; align-items:center; justify-content:center; font-size:45px; flex-shrink:0; }}
.green  {{ background:#D8EBCF; }}
.purple {{ background:#E5D8F2; }}
.orange {{ background:#F7DFC8; }}
.pink   {{ background:#F7D7DD; }}
.card-content {{ display:flex; flex-direction:column; justify-content:center; width:100%; margin:0; padding:0; }}
.card-content * {{ margin-left:0; }}
.card-content h3 {{ margin:0; font-size:{card_title_size}; color:#111; }}
.card-content p  {{ margin-top:8px; font-size:{body_size}; line-height:1.6; color:#555; }}

.view-button {{ background:#E3F2DB; border:2px solid #9ED492; border-radius:20px; padding:18px 30px; margin:35px auto 10px auto; width:320px; height:68px; display:flex; align-items:center; justify-content:center; position:relative; font-size:{button_size}; font-weight:700; color:#3D6B32; transition:0.2s; box-shadow:0 4px 10px rgba(0,0,0,0.04); }}
.view-button span {{ position:absolute; right:28px; top:50%; transform:translateY(-50%); font-size:24px; line-height:1; }}
.view-button:hover {{ transform:translateY(-2px); background:#F8FFF5; box-shadow:0 8px 18px rgba(0,0,0,0.08); }}

a {{ text-decoration:none !important; color:inherit !important; }}

.setting-label {{ font-size:{body_size}; font-weight:700; color:#0D1B3D; margin-bottom:8px; }}
[data-testid="stSelectbox"] {{ width: 280px !important; max-width: 280px; }}
[data-testid="stRadio"] {{ width: 240px !important; background:white; border:2px solid #D8D2C7; border-radius:18px; padding:6px 12px; }}
div[role="radiogroup"] label p {{ color:#0D1B3D !important; font-weight:600 !important; }}
[data-baseweb="select"] > div {{ background-color: white !important; border: 2px solid #D8D2C7 !important; border-radius: 18px !important; color: #222 !important; }}
[data-baseweb="select"] span {{ color: #222 !important; font-weight: 500;}}

/* ---MOBILE FIXES--- */
@media (max-width: 768px) {{
    html, body, [data-testid="stAppViewContainer"] {{ overflow-x: hidden !important; }}
    .block-container {{ padding-left: 1rem !important; padding-right: 1rem !important; padding-top: 1rem !important; max-width: 100% !important;}}
    
    .title,
    .page-title {{ font-size: {mobile_page_title_size} !important; line-height: 1.1 !important; word-break: normal !important; overflow-wrap: normal !important; }}
    h1, h2, h3 {{ word-break: normal !important; overflow-wrap: normal !important;}}

    .subtitle,
    .subtitle-box,
    .intro-box,
    .info-box,
    .tip-box {{
        font-size: {mobile_body_size} !important;
        padding: 16px 18px !important;
        border-radius: 20px !important;
        max-width: 100% !important;
        box-sizing: border-box !important;
    }}

    .announcement-card {{ flex-direction: column !important; align-items: center !important; text-align: center !important; padding: 20px !important; max-width: 100% !important; box-sizing: border-box !important; }}

    .icon-box {{ width: 80px !important; height: 80px !important; font-size: 34px !important; }}

    .card-content h3 {{ font-size: {mobile_card_title_size} !important; line-height: 1.25 !important; }}

    .card-content p {{ font-size: {mobile_body_size} !important; line-height: 1.45 !important;}}

    .view-button {{font-size: {mobile_button_size} !important; }}

    .form-card,
    .help-card,
    .request-card,
    .contact-card {{
        width: 100% !important;
        max-width: 100% !important;
        box-sizing: border-box !important;
    }}

    input, textarea, select {{ max-width: 100% !important; box-sizing: border-box !important;}}

    [data-testid="stSelectbox"],
    [data-testid="stRadio"] {{
        width: 100% !important;
        max-width: 100% !important;
    }}

    .stButton > button {{ font-size: 16px !important; padding: 10px 14px !important; margin-bottom: 20px !important; }}
}}

</style>
""", unsafe_allow_html=True)

st.markdown(apply_rtl_css(lang), unsafe_allow_html=True)

### TOP BAR
top_left, spacer, top_right = st.columns([2, 0.3, 1.7])

with top_left:
    if st.button(t("ann_back", lang)):
        st.query_params["text_size"] = st.session_state["text_size"]
        st.query_params["lang"] = lang
        st.switch_page("app.py")

with top_right:
    acc1, acc2 = st.columns([1.2, 1])

    with acc1:
        st.markdown(f"<div class='setting-label'>{t('label_language', lang)}</div>", unsafe_allow_html=True)

        selected_display = st.selectbox(
            "Language",
            LANGUAGE_OPTIONS,
            index=LANGUAGE_OPTIONS.index(next(k for k, v in LANGUAGE_MAP.items() if v == lang)),
            label_visibility="collapsed",
            key="ann_language_select"
        )

        new_lang = LANGUAGE_MAP[selected_display]

        if new_lang != st.session_state["language"]:
            st.session_state["language"] = new_lang
            st.query_params["lang"] = new_lang
            st.rerun()

    with acc2:
        st.markdown(f"<div class='setting-label'>{t('label_textsize', lang)}</div>", unsafe_allow_html=True)

        text_size = st.radio(
            "Text size",
            ["S", "M", "L"],
            index=["S", "M", "L"].index(st.session_state["text_size"]),
            horizontal=True,
            label_visibility="collapsed",
            key="ann_text_size_radio"
        )

        if text_size != st.session_state["text_size"]:
            st.session_state["text_size"] = text_size
            st.query_params["text_size"] = text_size
            st.rerun()

### HEADER
st.markdown(f'<div class="page-title">{t("ann_title", lang)}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="subtitle-box">{t("ann_subtitle", lang)}</div>', unsafe_allow_html=True)

### ANNOUNCEMENTS
announcement_data = [
    ("🌳", "green",  "ann_1_title", "ann_1_text"),
    ("🚌", "purple", "ann_2_title", "ann_2_text"),
    ("🚧", "orange", "ann_3_title", "ann_3_text"),
    ("❤️", "pink",   "ann_4_title", "ann_4_text"),
]

for icon, colour, title_key, text_key in announcement_data:
    st.markdown(f"""
<div class="announcement-card">
  <div class="icon-box {colour}">{icon}</div>
  <div class="card-content">
    <h3>{t(title_key, lang)}</h3>
    <p>{t(text_key, lang)}</p>
  </div>
</div>
""", unsafe_allow_html=True)

### VIEW ALL BUTTON
st.markdown(f"""
<a href="https://www.birmingham.gov.uk/" target="_blank">
  <div class="view-button">
    <div>{t("ann_view_all", lang)}</div>
    <span>→</span>
  </div>
</a>
""", unsafe_allow_html=True)