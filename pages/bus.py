### IMPORTS
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import streamlit as st
import folium
from streamlit_folium import st_folium
from translations import t, apply_rtl_css

st.set_page_config(page_title="Bus - Ladywood Connect", layout="wide")

# ── Language: read from URL first, then session state ──
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

if "text_size" not in st.session_state:
    st.session_state["text_size"] = "A"

text_size = st.session_state["text_size"]

if text_size == "A":
    page_title_size = "58px"
    section_title_size = "28px"
    body_size = "18px"
elif text_size == "A+":
    page_title_size = "70px"
    section_title_size = "34px"
    body_size = "22px"
else:
    page_title_size = "82px"
    section_title_size = "40px"
    body_size = "26px"

### CUSTOM CSS
st.markdown(f"""
<style>
[data-testid="stAppViewContainer"] {{ background-color: #F5F2EA; }}
[data-testid="stHeader"]           {{ background-color: transparent; }}
[data-testid="stSidebar"]          {{ display: none; }}
.block-container {{ padding-top: 2rem; padding-bottom: 2rem; }}

.stButton > button {{ background:white; border-radius:18px; border:2px solid #D8D2C7; padding:12px 18px; font-size:18px; color:#444; margin-bottom:25px; }}

.page-title    {{ font-size:{page_title_size}; font-weight:900; color:#0D1B3D; margin-bottom:5px; }}
.section-title {{ font-size:{section_title_size}; font-weight:700; color:#0D1B3D; margin-top:30px; margin-bottom:10px; }}
.info-box      {{ background:#DDB8E8; border:2px solid #c99de0; border-radius:24px; padding:20px 28px; margin-bottom:20px; font-size:{body_size}; color:#2a1a3e; }}
.live-badge    {{ display:inline-block; background:#CFEAC2; color:#2a6e1f; font-weight:700; font-size:16px; border-radius:20px; padding:6px 18px; margin-bottom:16px; border:2px solid #a8d8a0; }}
.schedule-box  {{ background:#C8E2F5; border:2px solid #a0c8e8; border-radius:24px; padding:20px 28px; margin-bottom:10px; }}
.tip-box       {{ background:#F4D2BD; border:2px solid #e0b89a; border-radius:24px; padding:20px 28px; margin-top:20px; font-size:{body_size}; color:#5a2e0e; }}
.day-row       {{ display:flex; justify-content:space-between; align-items:center; padding:10px 0; border-bottom:1px solid #b8d4e8; font-size:{body_size}; color:#0D1B3D; }}
.day-name      {{ font-weight:700; width:120px; }}
.day-time      {{ color:#444; }}
.closed        {{ color:#cc4444; font-weight:600; }}
a {{ text-decoration:none !important; color:inherit !important; }}

.setting-label {{ font-size:{body_size}; font-weight:700; color:#0D1B3D; margin-bottom:8px; }}
[data-testid="stSelectbox"] {{ width: 280px !important; max-width: 280px; }}
[data-testid="stRadio"] {{ width: 240px !important; background:white; border:2px solid #D8D2C7; border-radius:18px; padding:6px 12px; }}
div[role="radiogroup"] label p {{ color:#0D1B3D !important; font-weight:600 !important; }}
[data-baseweb="select"] > div {{ background-color: white !important; border: 2px solid #D8D2C7 !important; border-radius: 18px !important; color: #222 !important; }}
[data-baseweb="select"] span {{ color: #222 !important; font-weight: 500; }}
</style>
""", unsafe_allow_html=True)

st.markdown(apply_rtl_css(lang), unsafe_allow_html=True)

### TOP BAR
top_left, spacer, top_right = st.columns([2, 0.3, 1.7])

with top_left:
    if st.button(t("bus_back", lang)):
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
            key="bus_language_select"
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
            ["A", "A+", "A++"],
            index=["A", "A+", "A++"].index(st.session_state["text_size"]),
            horizontal=True,
            label_visibility="collapsed",
            key="bus_text_size_radio"
        )

        if text_size != st.session_state["text_size"]:
            st.session_state["text_size"] = text_size
            st.rerun()

### TITLE
st.markdown(f'<div class="page-title">{t("bus_title", lang)}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="info-box">{t("bus_info", lang)}</div>', unsafe_allow_html=True)

### LIVE LOCATION
st.markdown(f'<div class="section-title">{t("bus_where", lang)}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="live-badge">{t("bus_live_badge", lang)}</div>', unsafe_allow_html=True)

bus_lat, bus_lon = 52.47927, -1.91598
m = folium.Map(location=[bus_lat, bus_lon], zoom_start=16, tiles="OpenStreetMap")
folium.CircleMarker(location=[bus_lat, bus_lon], radius=30, color="#DDB8E8", fill=True, fill_color="#DDB8E8", fill_opacity=0.5).add_to(m)
folium.Marker(
    location=[bus_lat, bus_lon],
    popup=folium.Popup("""
        <div style='font-family:sans-serif;text-align:center;padding:5px;'>
            <h3 style='color:#6a0dad;margin:0;'>🚌 Community Bus</h3>
            <p style='margin:5px 0;'>📍 Ladywood Leisure Centre</p>
            <p style='margin:5px 0;'>⏰ Mon–Fri: 9:00–16:00</p>
            <p style='margin:5px 0;color:#cc4444;'>❌ Closed weekends</p>
        </div>
    """, max_width=220),
    tooltip="🚌 Community Bus — click for info!",
    icon=folium.Icon(color="purple", icon="bus", prefix="fa")
).add_to(m)
st_folium(m, width="100%", height=420)

st.markdown(f'<div class="info-box" style="background:#CFEAC2;border-color:#a8d8a0;color:#1a3e1a;">{t("bus_address", lang)}</div>', unsafe_allow_html=True)

### WEEKLY SCHEDULE
st.markdown(f'<div class="section-title">{t("bus_hours_title", lang)}</div>', unsafe_allow_html=True)

days = [
    ("bus_monday",    "⏰ 9:00 – 16:00", False),
    ("bus_tuesday",   "⏰ 9:00 – 16:00", False),
    ("bus_wednesday", "⏰ 9:00 – 16:00", False),
    ("bus_thursday",  "⏰ 9:00 – 16:00", False),
    ("bus_friday",    "⏰ 9:00 – 16:00", False),
    ("bus_saturday",  None,               True),
    ("bus_sunday",    None,               True),
]

rows_html = ""
for i, (day_key, time_str, closed) in enumerate(days):
    border = "" if i < len(days) - 1 else "border-bottom:none;"
    if closed:
        time_html = f'<span class="day-time closed">{t("bus_closed", lang)}</span>'
    else:
        time_html = f'<span class="day-time">{time_str}</span>'
    rows_html += f'<div class="day-row" style="{border}"><span class="day-name">{t(day_key, lang)}</span>{time_html}</div>'

st.markdown(f'<div class="schedule-box">{rows_html}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="tip-box">{t("bus_tip", lang)}</div>', unsafe_allow_html=True)