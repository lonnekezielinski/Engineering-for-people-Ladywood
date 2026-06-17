import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import streamlit as st
from translations import t
from styling import apply_style

# Page configuration
st.set_page_config(page_title="Announcements", layout="wide")

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

# Header
st.markdown(f'<div class="page-title">{t("ann_title", lang)}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="subtitle-box">{t("ann_subtitle", lang)}</div>', unsafe_allow_html=True)

# Announcements
announcement_data = [
    ("🚌", "purple", "ann_1_title", "ann_1_text"),
    ("🏠", "green",  "ann_2_title", "ann_2_text"),
    ("🎥", "blue",   "ann_3_title", "ann_3_text"),
    ("🍽️", "pink",  "ann_4_title", "ann_4_text"),
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

# View all announcements button
st.markdown(f"""
<a href="https://civicsquare.cc/" target="_blank">
  <div class="view-button">
    <div>{t("ann_view_all", lang)}</div>
    <span>→</span>
  </div>
</a>
""", unsafe_allow_html=True)