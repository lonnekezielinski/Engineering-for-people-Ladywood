### IMPORTS
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import streamlit as st
from translations import t, apply_rtl_css

### PAGE CONFIG
st.set_page_config(page_title="Feedback & Requests", layout="wide")

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
    panel_title_size = "28px"
    body_size = "18px"
elif text_size == "A+":
    page_title_size = "70px"
    panel_title_size = "34px"
    body_size = "22px"
else:
    page_title_size = "82px"
    panel_title_size = "40px"
    body_size = "26px"

### CUSTOM CSS
st.markdown(f"""
<style>
[data-testid="stAppViewContainer"] {{ background-color:#F5F2EA; }}
[data-testid="stHeader"]           {{ background:transparent; }}
[data-testid="stSidebar"]          {{ display:none; }}
.block-container {{ padding-top:2rem; padding-bottom:2rem; padding-left:3rem; padding-right:3rem; }}

.stButton > button {{ background:white; border-radius:18px; border:2px solid #D8D2C7; padding:12px 18px; font-size:18px; color:#444; margin-bottom:25px; }}

.page-title  {{ font-size:{page_title_size}; font-weight:900; color:#0D1B3D; margin-bottom:8px; }}
.intro-box   {{ background:#F4D2BD; border:2px solid #E4B999; border-radius:24px; padding:22px 28px; margin-bottom:30px; font-size:{body_size}; color:#5A2E0E; line-height:1.5; }}

.panel       {{ background:white; border:2px solid rgba(0,0,0,0.06); border-radius:28px; padding:28px; margin-bottom:25px; box-shadow:0 4px 12px rgba(0,0,0,0.04); }}
.panel-title {{ font-size:{panel_title_size}; font-weight:800; color:#0D1B3D; margin-bottom:20px; }}
.help-row    {{ display:flex; gap:18px; align-items:flex-start; margin-bottom:24px; }}
.help-icon   {{ width:64px; height:64px; border-radius:50%; display:flex; align-items:center; justify-content:center; font-size:30px; flex-shrink:0; }}
.blue   {{ background:#D9ECFA; }}
.green  {{ background:#D8EBCF; }}
.purple {{ background:#E5D8F2; }}
.orange {{ background:#F7DFC8; }}
.help-title {{ font-size:{body_size}; font-weight:800; color:#0D1B3D; }}
.help-text  {{ font-size:{body_size}; color:#444; }}

.request-card  {{ background:#FAFAFA; border:2px solid rgba(0,0,0,0.06); border-radius:20px; padding:18px; margin-bottom:14px; display:flex; align-items:center; gap:18px; }}
.request-icon  {{ width:64px; height:64px; border-radius:16px; display:flex; align-items:center; justify-content:center; font-size:32px; flex-shrink:0; }}
.request-title {{ font-size:{body_size}; font-weight:800; color:#0D1B3D; }}
.request-meta  {{ font-size:{body_size}; color:#555; margin-top:4px; }}
.status        {{ margin-left:auto; padding:8px 14px; border-radius:18px; font-size:14px; font-weight:700; }}
.in-progress   {{ background:#D9ECFA; color:#1C6BB0; }}
.under-review  {{ background:#F7DFC8; color:#A35E00; }}
.completed     {{ background:#D8EBCF; color:#287A3E; }}
.closed        {{ background:#E8E8E8; color:#555; }}

div[data-baseweb="select"] > div, textarea, input {{ border-radius:16px !important; }}
.stTextArea textarea {{ min-height:170px; }}

div[data-testid="stFormSubmitButton"] button {{ width:100%; background:#7B3FB2; color:white; border:none; border-radius:16px; padding:16px; font-size:20px; font-weight:700; }}
div[data-testid="stFormSubmitButton"] button:hover {{ background:#6A329E; color:white; }}

.stTabs [data-baseweb="tab-list"]  {{ gap:14px; margin-bottom:30px; border-bottom:2px solid #D8D2C7; }}
.stTabs [data-baseweb="tab"]       {{ background:#F5F2EA; border:2px solid #D8D2C7; border-bottom:none; border-radius:18px 18px 0 0; padding:14px 32px; font-size:30px; font-weight:700; color:#555; height:65px; }}
.stTabs [data-baseweb="tab"] p     {{ font-size:18px; }}
.stTabs [aria-selected="true"]     {{ background:white !important; color:#7B3FB2 !important; border-bottom:5px solid #7B3FB2 !important; }}

input, textarea, [data-baseweb="select"] > div {{ background-color:white !important; color:#0D1B3D !important; border:2px solid #D8D2C7 !important; }}
textarea::placeholder, input::placeholder {{ color:#777 !important; }}

[data-testid="stSelectbox"] label p,
[data-testid="stTextArea"] label p,
[data-testid="stTextInput"] label p {{ color:#0D1B3D !important; font-weight:700 !important; font-size:17px !important; }}

[data-testid="stAlert"]   {{ background-color:#D8EBCF !important; border:2px solid #9ED18F !important; border-radius:18px !important; }}
[data-testid="stAlert"] p {{ color:#1E4D2B !important; font-size:18px !important; font-weight:700 !important; }}

.setting-label {{ font-size:{body_size}; font-weight:700; color:#0D1B3D; margin-bottom:8px; }}
[data-testid="stSelectbox"] {{ width: 280px !important; max-width: 280px; }}
[data-testid="stRadio"] {{ width: 240px !important; background:white; border:2px solid #D8D2C7; border-radius:18px; padding:6px 12px; }}
div[role="radiogroup"] label p {{ color:#0D1B3D !important; font-weight:600 !important; }}
[data-baseweb="select"] > div {{ background-color:white !important; border:2px solid #D8D2C7 !important; border-radius:18px !important; color:#222 !important; }}
[data-baseweb="select"] span {{ color:#222 !important; font-weight:500; }}

/* ---MOBILE FIXES--- */
@media (max-width: 768px) {{
    html, body, [data-testid="stAppViewContainer"] {{ overflow-x: hidden !important; }}
    .block-container {{ padding-left: 1rem !important; padding-right: 1rem !important; padding-top: 1rem !important; max-width: 100% !important;}}
    
    .title,
    .page-title {{ font-size: 40px !important; line-height: 1.1 !important; word-break: normal !important; overflow-wrap: normal !important; }}
    h1, h2, h3 {{ word-break: normal !important; overflow-wrap: normal !important;}}

    .subtitle,
    .subtitle-box,
    .intro-box,
    .info-box,
    .tip-box {{
        font-size: 16px !important;
        padding: 16px 18px !important;
        border-radius: 20px !important;
        max-width: 100% !important;
        box-sizing: border-box !important;
    }}

    .announcement-card {{ flex-direction: column !important; align-items: center !important; text-align: center !important; padding: 20px !important; max-width: 100% !important; box-sizing: border-box !important; }}

    .icon-box {{ width: 80px !important; height: 80px !important; font-size: 34px !important; }}

    .card-content h3 {{ font-size: 22px !important; line-height: 1.25 !important; }}

    .card-content p {{ font-size: 16px !important; line-height: 1.45 !important;}}

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
    if st.button(t("fb_back", lang)):
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
            ["A", "A+", "A++"],
            index=["A", "A+", "A++"].index(st.session_state["text_size"]),
            horizontal=True,
            label_visibility="collapsed",
            key="fb_text_size_radio"
        )

        if text_size != st.session_state["text_size"]:
            st.session_state["text_size"] = text_size
            st.rerun()

### HEADER
st.markdown(f'<div class="page-title">{t("fb_title", lang)}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="intro-box">{t("fb_intro", lang)}</div>', unsafe_allow_html=True)

### TABS
feedback_tab, requests_tab = st.tabs([t("fb_tab_feedback", lang), t("fb_tab_requests", lang)])

# ── Feedback tab ──
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
<div class="request-card"><div class="request-icon orange">📪</div><div><div class="request-title">Fill in the form at the Community Bus</div></div></div>
</div>
""", unsafe_allow_html=True)

# ── Requests tab ──
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
<div class="panel-title">{t("fb_your_requests", lang)}</div>
<div style="font-size:17px;color:#555;margin-bottom:20px;">{t("fb_your_requests_sub", lang)}</div>
<div class="request-card"><div class="request-icon orange">🚌</div><div><div class="request-title">Request for better bus shelter</div><div class="request-meta">Transport · 5 days ago</div></div><div class="status in-progress">In progress</div></div>
<div class="request-card"><div class="request-icon green">🌳</div><div><div class="request-title">Fix lighting in the park</div><div class="request-meta">Parks · 1 week ago</div></div><div class="status under-review">Under review</div></div>
<div class="request-card"><div class="request-icon purple">👥</div><div><div class="request-title">Request for youth activities</div><div class="request-meta">Community · 2 weeks ago</div></div><div class="status completed">Completed</div></div>
<div class="request-card"><div class="request-icon orange">🗑️</div><div><div class="request-title">More frequent bin collection</div><div class="request-meta">Waste · 2 weeks ago</div></div><div class="status closed">Closed</div></div>
<div style="text-align:center;margin-top:20px;font-weight:700;color:#7B3FB2;">{t("fb_view_all", lang)}</div>
</div>
""", unsafe_allow_html=True)