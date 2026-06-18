import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import streamlit as st
import folium
from streamlit_folium import st_folium
from translations import t
from styling import apply_style

# Page configuration
st.set_page_config(page_title="Bus - Ladywood Connect", layout="wide")

# Language settings
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
apply_style(lang)

# Top bar
top_left, spacer, top_right = st.columns([2, 0.3, 1.7])

with top_left:
    if st.button(t("bus_back", lang)):
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
            ["S", "M", "L"],
            index=["S", "M", "L"].index(st.session_state["text_size"]),
            horizontal=True,
            label_visibility="collapsed",
            key="bus_text_size_radio"
        )

        if text_size != st.session_state["text_size"]:
            st.session_state["text_size"] = text_size
            st.query_params["text_size"] = text_size
            st.rerun()

# Header
st.markdown(f'<div class="page-title">{t("bus_title", lang)}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="info-box">{t("bus_info", lang)}</div>', unsafe_allow_html=True)

# Live location
st.markdown(f'<div class="section-title">{t("bus_where", lang)}</div>', unsafe_allow_html=True)

bus_lat, bus_lon = 52.475583, -1.928278 
m = folium.Map(location=[bus_lat, bus_lon], zoom_start=16, tiles="OpenStreetMap")
folium.CircleMarker(location=[bus_lat, bus_lon], radius=30, color="#DDB8E8", fill=True, fill_color="#DDB8E8", fill_opacity=0.5).add_to(m)
folium.Marker(
    location=[bus_lat, bus_lon],
    popup=folium.Popup(f"""
    <div style='font-family:sans-serif;text-align:center;padding:5px;'>
        <h3 style='color:#6a0dad;margin:0;'>{t("bus_map_title", lang)}</h3>
        <p style='margin:5px 0;'>{t("bus_map_place", lang)}</p>
        <p style='margin:5px 0;'>{t("bus_map_hours", lang)}</p>
    </div>
""", max_width=220),
tooltip=t("bus_map_tooltip", lang),
    icon=folium.Icon(color="purple", icon="bus", prefix="fa")
).add_to(m)

# Right column with information and also make two columns so that the map becomes smaller 
map_col, info_col = st.columns([1.7, 1])

with map_col:
    st_folium(m, width="100%", height=400)

with info_col:
    st.image("assets/outside-bus-dashboard.png")

col1, col2 = st.columns([1, 1])
with col1:
    st.markdown(f"""
    <div class="bus-location-box">
        <div class="bus-location-icon">📍</div>
        <div>
            <h3>{t("bus_live_badge", lang)}</h3>
            <p>{t("bus_address", lang)}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="workshop-redirect-box">
        <div class="workshop-redirect-icon">🧑‍💻</div>
        <div>
            <h3>{t('bus_wanttojoinaworkshop', lang)}</h3>
            <p>{t('bus_seecommunityoffers', lang)}</p>
            <a href="workshops?lang={lang}&text_size={st.session_state['text_size']}" target="_self">
                View workshops →
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Weekly schedule 
st.markdown(f'<div class="section-title">{t("bus_hours_title", lang)}</div>', unsafe_allow_html=True)

days = [
    ("bus_monday",    "⏰ 7:00 – 12:00 & 13:00 - 18:00"),
    ("bus_tuesday",   "⏰ 7:00 – 12:00 & 13:00 - 18:00"),
    ("bus_wednesday", "⏰ 7:00 – 12:00 & 13:00 - 18:00"),
    ("bus_thursday",  "⏰ 7:00 – 12:00 & 13:00 - 18:00"),
    ("bus_friday",    "⏰ 7:00 – 12:00 & 13:00 - 18:00"),
    ("bus_saturday",  "⏰ 7:00 – 12:00 & 13:00 - 18:00"),
    ("bus_sunday",    "⏰ 7:00 – 12:00 & 13:00 - 18:00"),
]

rows_html = ""
for i, (day_key, time_str) in enumerate(days):
    border = "" if i < len(days) - 1 else "border-bottom:none;"
    rows_html += (
        f'<div class="day-row" style="{border}">'
        f'<span class="day-name">{t(day_key, lang)}</span>'
        f'<span class="day-time">{time_str}</span>'
        f'</div>'
    )
st.markdown(f'<div class="schedule-box">{rows_html}</div>', unsafe_allow_html=True)