import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import streamlit as st
from translations import t
from styling import apply_style

# Page configuration
st.set_page_config(page_title="Feedback & Requests", layout="wide")

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
    if st.button(t("fb_back", lang)):
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
            key="fb_language_select"
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
            key="fb_text_size_radio"
        )

        if text_size != st.session_state["text_size"]:
            st.session_state["text_size"] = text_size
            st.query_params["text_size"] = text_size
            st.rerun()

# Header
st.markdown(f'<div class="page-title">{t("fb_title", lang)}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="intro-box">{t("fb_intro", lang)}</div>', unsafe_allow_html=True)

feedback_tab, requests_tab = st.tabs([t("fb_tab_feedback", lang), t("fb_tab_requests", lang)])

# Feedback tab
with feedback_tab:
    left, right = st.columns([1.1, 1])
    with left:
        st.markdown(f'<div class="panel-title">{t("fb_form_title", lang)}</div>', unsafe_allow_html=True)
        with st.form("feedback_form"):
            feedback_topic = st.selectbox(t("fb_topic_label", lang), t("fb_topic_options", lang))
            feedback_text  = st.text_area(t("fb_text_label", lang), placeholder=t("fb_text_placeholder", lang))
            feedback_name  = st.text_input(t("fb_name_label", lang), placeholder=t("fb_name_placeholder", lang))
            submitted = st.form_submit_button(t("fb_submit", lang))
            if submitted:
                st.success(t("fb_success", lang))

    with right:
        st.markdown(f"""
<div class="panel">
<div class="panel-title">{t("fb_next_title", lang)}</div>
<div class="help-row"><div class="help-icon blue">🔍</div><div><div class="help-title">{t("fb_next_1_title", lang)}</div><div class="help-text">{t("fb_next_1_text", lang)}</div></div></div>
<div class="help-row"><div class="help-icon green">✅</div><div><div class="help-title">{t("fb_next_2_title", lang)}</div><div class="help-text">{t("fb_next_2_text", lang)}</div></div></div>
<div class="help-row"><div class="help-icon purple">📢</div><div><div class="help-title">{t("fb_next_3_title", lang)}</div><div class="help-text">{t("fb_next_3_text", lang)}</div></div></div>
</div>
""", unsafe_allow_html=True)

        st.markdown(f"""
<div class="panel">
<div class="panel-title">{t("fb_contact_title", lang)}</div>
<div class="request-card"><div class="request-icon orange">📞</div><div><div class="request-title">0121 345 6789</div></div></div>
<div class="request-card"><div class="request-icon orange">✉️</div><div><div class="request-title">info@ladywoodconnect.org</div></div></div>
<div class="request-card"><div class="request-icon orange">📪</div><div><div class="request-title">{t("fb_contact_bus_form", lang)}</div></div></div>
</div>
""", unsafe_allow_html=True)

# Requests tab
with requests_tab:
    left, right = st.columns([1.1, 1])
    with left:
        st.markdown(f'<div class="panel-title">{t("fb_req_form_title", lang)}</div>', unsafe_allow_html=True)
        with st.form("request_form"):
            request_topic = st.selectbox(t("fb_req_topic_label", lang), t("fb_req_topic_options", lang))
            request_text  = st.text_area(t("fb_req_text_label", lang), placeholder=t("fb_req_text_placeholder", lang))
            request_name  = st.text_input(t("fb_req_name_label", lang), placeholder=t("fb_req_name_placeholder", lang))
            request_submitted = st.form_submit_button(t("fb_req_submit", lang))
            if request_submitted:
                st.success(t("fb_req_success", lang))
    
    with right:
        st.markdown(f"""
    <div class="panel">
    <div class="panel-title">{t("fb_next_title", lang)}</div>
    <div class="help-row"><div class="help-icon blue">🔍</div><div><div class="help-title">{t("fb_next_1_title", lang)}</div><div class="help-text">{t("fb_next_1_text", lang)}</div></div></div>
    <div class="help-row"><div class="help-icon green">✅</div><div><div class="help-title">{t("fb_next_2_title", lang)}</div><div class="help-text">{t("fb_next_2_text", lang)}</div></div></div>
    <div class="help-row"><div class="help-icon purple">📢</div><div><div class="help-title">{t("fb_next_3_title", lang)}</div><div class="help-text">{t("fb_next_3_text", lang)}</div></div></div>
    </div>
    """, unsafe_allow_html=True)

        st.markdown(f"""
    <div class="panel">
    <div class="panel-title">{t("fb_contact_title", lang)}</div>
    <div class="request-card"><div class="request-icon orange">📞</div><div><div class="request-title">0121 345 6789</div></div></div>
    <div class="request-card"><div class="request-icon orange">✉️</div><div><div class="request-title">info@ladywoodconnect.org</div></div></div>
    <div class="request-card"><div class="request-icon orange">📪</div><div><div class="request-title">{t("fb_contact_bus_form", lang)}</div></div></div>
    </div>
    """, unsafe_allow_html=True)