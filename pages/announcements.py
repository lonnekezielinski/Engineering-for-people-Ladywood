### IMPORTS
import streamlit as st
import base64
from translations import t, apply_rtl_css

### PAGE CONFIG
st.set_page_config(page_title="Announcements", layout="wide")
# Read language from URL or session state
if "lang" in st.query_params:
    url_lang = st.query_params["lang"]
    if url_lang in ["English", "Arabic", "Urdu", "Punjabi"]:
        st.session_state["language"] = url_lang

lang = st.session_state.get("language", "English")

### FUNCTION FOR PNG ICON
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

announcement_icon = get_base64_image("assets/megaphone.png")

### CUSTOM CSS
st.markdown("""
<style>
[data-testid="stAppViewContainer"] { background-color: #F5F2EA; }
[data-testid="stHeader"]           { background: transparent; }
[data-testid="stToolbar"]          { right: 2rem; }
[data-testid="stSidebar"]          { display: none; }
.block-container { max-width:none; width:100%; padding-top:2rem; padding-bottom:2rem; padding-left:4rem; padding-right:4rem; }

.stButton > button { background:white; border-radius:18px; border:2px solid #D8D2C7; padding:12px 18px; font-size:18px; color:#444; margin-bottom:25px; }

.page-title    { font-size:58px; font-weight:900; color:#0D1B3D; margin-bottom:5px; }
.page-subtitle { font-size:20px; color:#555; margin-bottom:30px; }

.subtitle-box { background:#CFEAC2; border:2px solid #A8D8A0; border-radius:24px; padding:20px 28px; margin-bottom:30px; font-size:18px; color:#1A3E1A; }

.announcement-card { background:white; border-radius:28px; padding:22px; margin-bottom:22px; display:flex; flex-direction:row; align-items:center; gap:24px; border:2px solid rgba(0,0,0,0.05); box-shadow:0 4px 12px rgba(0,0,0,0.04); transition:0.2s; }
.announcement-card:hover { transform:scale(1.01); }
.icon-box { width:110px; height:110px; border-radius:25px; display:flex; align-items:center; justify-content:center; font-size:45px; flex-shrink:0; }
.green  { background:#D8EBCF; }
.purple { background:#E5D8F2; }
.orange { background:#F7DFC8; }
.pink   { background:#F7D7DD; }
.card-content { display:flex; flex-direction:column; justify-content:center; width:100%; margin:0; padding:0; }
.card-content * { margin-left:0; }
.card-content h3 { margin:0; font-size:28px; color:#111; }
.card-content p  { margin-top:8px; font-size:18px; line-height:1.6; color:#555; }

.view-button { background:#E3F2DB; border:2px solid #9ED492; border-radius:20px; padding:18px 30px; margin:35px auto 10px auto; width:320px; height:68px; display:flex; align-items:center; justify-content:center; position:relative; font-size:20px; font-weight:700; color:#3D6B32; transition:0.2s; box-shadow:0 4px 10px rgba(0,0,0,0.04); }
.view-button span { position:absolute; right:28px; top:50%; transform:translateY(-50%); font-size:24px; line-height:1; }
.view-button:hover { transform:translateY(-2px); background:#F8FFF5; box-shadow:0 8px 18px rgba(0,0,0,0.08); }

a { text-decoration:none !important; color:inherit !important; }
</style>
""", unsafe_allow_html=True)

st.markdown(apply_rtl_css(lang), unsafe_allow_html=True)

### BACK BUTTON
if st.button(t("ann_back", lang)):
    st.switch_page("app.py")

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
