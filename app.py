import streamlit as st
from pathlib import Path
from translations import t
from styling import apply_style

# Page configuration
st.set_page_config(page_title="Ladywood Connect", layout="wide")

# Language 
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
apply_style(lang)

# Header
logo_path = Path("assets/waypoint-logo.png")

col_logo, col_title, col_lang, col_text = st.columns([0.09, 0.57, 0.17, 0.17], vertical_alignment="center")
with col_logo:
    st.image(str(logo_path), width=90)

with col_title:
    st.markdown(
        f'<div class="title">{t("app_title", lang)}</div>',
        unsafe_allow_html=True
    )

with col_lang:
    st.markdown(
        f"<div class='setting-label'>{t('label_language', lang)}</div>",
        unsafe_allow_html=True
    )

    selected_display = st.selectbox(
        "Language",
        LANGUAGE_OPTIONS,
        index=LANGUAGE_OPTIONS.index(
            next(k for k, v in LANGUAGE_MAP.items() if v == lang)
        ),
        label_visibility="collapsed",
        key="top_language_selectbox"
    )

    new_lang = LANGUAGE_MAP[selected_display]

    if new_lang != st.session_state["language"]:
        st.session_state["language"] = new_lang
        st.query_params["lang"] = new_lang
        st.rerun()

with col_text:
    st.markdown(
        f"<div class='setting-label'>{t('label_textsize', lang)}</div>",
        unsafe_allow_html=True
    )

    text_size_choice = st.radio(
        "Text size",
        ["S", "M", "L"],
        index=["S", "M", "L"].index(st.session_state["text_size"]),
        horizontal=True,
        label_visibility="collapsed",
        key="top_text_size_radio"
    )

    if text_size_choice != st.session_state["text_size"]:
        st.session_state["text_size"] = text_size_choice
        st.query_params["text_size"] = text_size_choice
        st.rerun()

st.markdown(
    f'<div class="subtitle">{t("app_subtitle", lang)}</div>',
    unsafe_allow_html=True
)

# Card grid
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
