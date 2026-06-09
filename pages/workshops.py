import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import streamlit as st
from translations import t, apply_rtl_css

st.set_page_config(page_title="Workshops", layout="wide")

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
    form_title_size = "1.8rem"

    mobile_page_title_size = "40px"
    mobile_body_size = "16px"
    mobile_form_title_size = "1.5rem"

elif text_size == "M":
    page_title_size = "70px"
    body_size = "22px"
    form_title_size = "2.2rem"

    mobile_page_title_size = "48px"
    mobile_body_size = "20px"
    mobile_form_title_size = "1.9rem"

elif text_size == "L":
    page_title_size = "82px"
    body_size = "26px"
    form_title_size = "2.6rem"

    mobile_page_title_size = "56px"
    mobile_body_size = "24px"
    mobile_form_title_size = "2.3rem"

### CUSTOM CSS
st.markdown(f"""
<style>
    [data-testid="stAppViewContainer"] {{background-color: #F5F2EA;}}
    [data-testid="stHeader"] {{background-color: transparent;}}
    .block-container {{padding-top: 1rem;}}
    #MainMenu, footer {{visibility: hidden;}}
    [data-testid="stSidebar"] {{ display:none; }}

    div[data-testid="stTextInput"] input {{ border-radius:50px !important; border:1.5px solid #e5e5e5 !important; padding:0.65rem 1.2rem !important; font-size:0.95rem !important; background:#fafafa !important; }}
    div[data-testid="stTextInput"] input:focus {{ border-color:#f7679a !important; background:white !important; box-shadow:0 0 0 3px rgba(247,103,154,0.1) !important; }}
    div[data-testid="stTextInput"] label {{ font-size:0.85rem !important; font-weight:500 !important; color:#444 !important; }}

    div[data-testid="stForm"] button[type="submit"] {{ background:#285C7A !important; color:white !important; border:none !important; border-radius:50px !important; padding:0.75rem 2rem !important; font-size:0.95rem !important; font-weight:500 !important; width:100% !important; cursor:pointer !important; margin-top:0.5rem !important; }}
    div[data-testid="stForm"] button[type="submit"]:hover {{ background:#333 !important; }}

    .stButton > button {{ background:white; border-radius:18px; border:2px solid #D8D2C7; padding:12px 18px; font-size:18px; color:#444; margin-bottom:25px; }}
    .intro-box {{ background:#C8E2F5; border:2px solid #9CC7E6; border-radius:24px; padding:22px 28px; margin-bottom:30px; font-size:19px; color:#285C7A; line-height:1.5; }}

    .page-title {{ font-size:{page_title_size}; font-weight:900; color:#0D1B3D; margin-bottom:10px; }}
    .intro-box {{ background:#C8E2F5; border:2px solid #9CC7E6; border-radius:24px; padding:22px 28px; margin-bottom:30px; font-size:{body_size}; color:#285C7A; line-height:1.5; }}
    .form-title {{ font-family:'Playfair Display',serif; font-size:{form_title_size}; font-weight:900; color:#1a1a1a; margin-bottom:0.3rem; }}
    .form-subtitle {{ font-size:{body_size}; color:#888; margin-bottom:2rem; }}
    .setting-label {{ font-size:{body_size}; font-weight:700; color:#0D1B3D; margin-bottom:8px; }}
    [data-testid="stRadio"] {{ width:240px !important; background:white; border:2px solid #D8D2C7; border-radius:18px; padding:6px 12px; }}
    div[role="radiogroup"] label p {{ color:#0D1B3D !important; font-weight:600 !important;}}
    [data-baseweb="select"] > div {{ background-color:white !important; border:2px solid #D8D2C7 !important; border-radius:18px !important; color:#222 !important; }}
    [data-baseweb="select"] span {{ color:#222 !important; font-weight:500; }}

    .theme-access {{
        background: #FFF1B8;
        color: #6B4E00;
    }}

    .theme-opportunity {{
        background: #D8EBCF;
        color: #2F6B32;
    }}

    .theme-confidence {{
        background: #D9ECFA;
        color: #285C7A;
    }}

    .side-card {{
        border: 2px solid rgba(0,0,0,0.06);
        border-radius: 32px;
        padding: 28px;
        font-size: 16px;
        line-height: 1.5;
        color: #0D1B3D;
    }}

    /* registration CSS */
    .registration-card {{
        background: white;
        border: 2px solid rgba(0,0,0,0.06);
        border-radius: 28px;
        padding: 32px;
        margin-top: 30px;
        margin-bottom: 40px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.04);
    }}

    .registration-title {{
        font-size: 34px;
        font-weight: 900;
        color: #0D1B3D;
        margin-bottom: 6px;
    }}

    .registration-subtitle {{
        font-size: 18px;
        color: #555;
        margin-bottom: 24px;
    }}

    [data-testid="stForm"] {{ background: transparent;}}

    [data-testid="stForm"] > div {{ padding: 0;}}

    [data-testid="stSelectbox"] {{
        width: 100% !important;
        max-width: 420px !important;
    }}

    div[data-testid="stFormSubmitButton"] button {{
        width: auto !important;
        min-width: 170px;
        background: #285C7A !important;
        color: white !important;
        border: none !important;
        border-radius: 18px !important;
        padding: 14px 24px !important;
        font-size: 18px !important;
        font-weight: 800 !important;
    }}

    .soft-card {{
        background: white !important;
        border-radius: 28px !important;
        padding: 32px !important;
        margin-bottom: 24px !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.04);
        display: flex;
        gap: 22px;
        align-items: flex-start;
    }}

    .soft-card .side-icon {{
        width: 64px;
        height: 64px;
        border-radius: 50%;
        background: #D9ECFA;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 30px;
        flex-shrink: 0;
    }}

    .theme-title {{
        font-weight: 900 !important;
    }}

    /* ---MOBILE FIXES--- */
    @media (max-width: 768px) {{
        html, body, [data-testid="stAppViewContainer"] {{ overflow-x: hidden !important; }}
        .block-container {{ padding-left: 1rem !important; padding-right: 1rem !important; padding-top: 1rem !important; max-width: 100% !important;}}
        
        .title, .page-title {{ font-size: {mobile_page_title_size} !important; line-height: 1.1 !important; word-break: normal !important; overflow-wrap: normal !important; }}
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

        .form-title {{ font-size: {mobile_form_title_size} !important; }}
        .form-subtitle {{ font-size: {mobile_body_size} !important; }}
        .form-section {{ padding: 1.5rem !important; max-width: 100% !important; }}
        .success-title {{ font-size: {mobile_body_size} !important; }}
        .success-text {{ font-size: {mobile_body_size} !important; }}

        input, textarea, select {{ max-width: 100% !important; box-sizing: border-box !important;}}

        [data-testid="stSelectbox"],
        [data-testid="stRadio"] {{
            width: 100% !important;
            max-width: 100% !important;
        }}

        .workshop-layout {{ grid-template-columns: 1fr; }}

        .stButton > button {{ font-size: 16px !important; padding: 10px 14px !important; margin-bottom: 20px !important; }}
    }}

    /* FIX workshop page text colours */
    .schedule-box h2,
    .registration-card,
    .registration-card label,
    .registration-card p,
    .registration-card div,
    .registration-card span,
    [data-testid="stForm"] label,
    [data-testid="stForm"] p {{
        color: #0D1B3D !important;
    }}

    /* FIX dark notes box */
    textarea {{
        background: white !important;
        color: #0D1B3D !important;
        border: 2px solid #1f2230 !important;
        border-radius: 14px !important;
    }}

    /* Make registration form look like one card */
    [data-testid="stForm"] {{
        background: white !important;
        border: 2px solid rgba(0,0,0,0.06) !important;
        border-radius: 28px !important;
        padding: 32px !important;
        margin-bottom: 40px !important;
    }}

    .schedule-main-title {{
        color: #0D1B3D !important;
        font-size: {form_title_size} !important;
        font-weight: 900 !important;
        line-height: 1.05 !important;
        margin-bottom: 16px !important;
        font-family: 'Playfair Display', serif;
    }}

    .compact-theme-row {{
        display: flex;
        justify-content: space-between;
        gap: 20px;
        align-items: center;
        padding: 14px 18px;
        border-radius: 14px;
        margin-bottom: 10px;
    }}

    .theme-title {{ font-weight: 900 !important; }}

    .theme-text {{ margin-top: 4px; }}

    .theme-time {{ font-weight: 900; white-space: nowrap; color: #0D1B3D; }}

    [data-testid="stExpander"] {{ border: none !important; border-bottom: 1px solid #EEE7DC !important; box-shadow: none !important; }}

    [data-testid="stExpander"] summary {{
        font-size: 22px !important;
        font-weight: 900 !important;
        color: #0D1B3D !important;
    }}

    div[data-testid="stFormSubmitButton"] button,
    div[data-testid="stFormSubmitButton"] button * {{
        color: white !important;
    }}

    /* Make the schedule a real white card */
    .schedule-card {{
        background: white !important;
        border-radius: 28px !important;
        padding: 32px !important;
        margin-bottom: 30px !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.04) !important;
        border: 2px solid rgba(0,0,0,0.06) !important;
    }}

    /* Fix invisible text */
    .schedule-note {{
        color: #4B5563 !important;
        font-size: 22px !important;
        }}
    .schedule-card p,
    .schedule-card div,
    .schedule-card span {{
        color: #0D1B3D !important;
    }}

    /* Make expander day rows white, not black */
    [data-testid="stExpander"] {{
        background: rgba(255,255,255,0.65) !important;
        border: 2px solid rgba(0,0,0,0.05) !important;
        border-bottom: 1px solid #EEE7DC !important;
        box-shadow: none !important;
    }}

    [data-testid="stExpander"] details,
    [data-testid="stExpander"] summary {{
        background: white !important;
        color: #0D1B3D !important;
    }}

    /* Bigger day text, no emoji styling needed */
    [data-testid="stExpander"] summary p {{
        font-size: 21px !important;
        font-weight: 900 !important;
        color: #0D1B3D !important;
    }}

    [data-testid="stExpander"] {{
        border-radius: 18px !important;
        overflow: hidden !important;
        margin-bottom: 16px !important;
    }}

    [data-testid="stExpander"] details {{
        border-radius: 18px !important;
        overflow: hidden !important;
    }}

    [data-testid="stExpander"] summary {{
        border-radius: 18px !important;
        padding-top: 8px !important;
        padding-bottom: 8px !important;
    }}

    .quick-note {{
        background: #F5F2EA;
        border: 2px solid #EEE7DC;
        border-radius: 20px;
        padding: 18px 22px;
        margin: 18px 0 28px 0;
        display: flex;
        gap: 16px;
        align-items: flex-start;
        color: #0D1B3D;
        font-size: 18px;
        line-height: 1.5;
    }}

    .quick-note-icon {{
        width: 44px;
        height: 44px;
        border-radius: 50%;
        background: #D9ECFA;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
    }}
</style>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

st.markdown(apply_rtl_css(lang), unsafe_allow_html=True)

### TOP BAR
top_left, spacer, top_right = st.columns([2, 0.3, 1.7])

with top_left:
    if st.button(t("ws_back", lang)):
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
            key="ws_language_select"
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
            key="ws_text_size_radio"
        )

        if text_size != st.session_state["text_size"]:
            st.session_state["text_size"] = text_size
            st.query_params["text_size"] = text_size
            st.rerun()

### HEADER
st.markdown(f'<div class="page-title">{t("ws_title", lang)}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="intro-box">{t("ws_subtitle", lang)}</div>', unsafe_allow_html=True)

### WORKSHOP SCHEDULE

left, right = st.columns([2.2, 1])

days = {
    "Monday": [
        ("10:00 AM – 11:30 AM", "Access", t("ws_mondayaccess", lang), "theme-access"),
        ("1:00 PM – 2:30 PM", "Opportunity", t("ws_mondayopportunity", lang), "theme-opportunity"),
        ("3:00 PM – 4:30 PM", "Confidence", t("ws_mondayconfidence", lang), "theme-confidence"),
    ],
    "Tuesday": [
        ("10:00 AM – 11:30 AM", "Access", t("ws_tuesdayaccess", lang), "theme-access"),
        ("1:00 PM – 2:30 PM", "Opportunity", t("ws_tuesdayopportunity", lang), "theme-opportunity"),
        ("3:00 PM – 4:30 PM", "Confidence", t("ws_tuesdayconfidence", lang), "theme-confidence"),
    ],
    "Wednesday": [
        ("10:00 AM – 11:30 AM", "Access", t("ws_wednesdayaccess", lang), "theme-access"),
        ("1:00 PM – 2:30 PM", "Opportunity", t("ws_wednesdayopportunity", lang), "theme-opportunity"),
        ("3:00 PM – 4:30 PM", "Confidence", t("ws_wednesdayconfidence", lang), "theme-confidence"),
    ],
    "Thursday": [
        ("10:00 AM – 11:30 AM", "Access", t("ws_thursdayaccess", lang), "theme-access"),
        ("1:00 PM – 2:30 PM", "Opportunity", t("ws_thursdayopportunity", lang), "theme-opportunity"),
        ("3:00 PM – 4:30 PM", "Confidence", t("ws_thursdayconfidence", lang), "theme-confidence"),
    ],
    "Friday": [
        ("10:00 AM – 11:30 AM", "Access", t("ws_fridayaccess", lang), "theme-access"),
        ("1:00 PM – 2:30 PM", "Opportunity", t("ws_fridayopportunity", lang), "theme-opportunity"),
        ("3:00 PM – 4:30 PM", "Confidence", t("ws_fridayconfidence", lang), "theme-confidence"),
    ],
    "Saturday": [
        ("10:00 AM – 11:30 AM", "Access", t("ws_saturdayaccess", lang), "theme-access"),
        ("1:00 PM – 2:30 PM", "Opportunity", t("ws_saturdayopportunity", lang), "theme-opportunity"),
        ("3:00 PM – 4:30 PM", "Confidence", t("ws_saturdayconfidence", lang), "theme-confidence"),
    ],
    "Sunday": [
        ("10:00 AM – 11:30 AM", "Access", t("ws_sundayaccess", lang), "theme-access"),
        ("1:00 PM – 2:30 PM", "Opportunity", t("ws_sundayopportunity", lang), "theme-opportunity"),
        ("3:00 PM – 4:30 PM", "Confidence", t("ws_sundayconfidence", lang), "theme-confidence"),
    ],
}

with left:
    st.markdown(f'<h2 class="schedule-main-title">{t("ws_schedule_title", lang)}</h2>', unsafe_allow_html=True)
    st.markdown(f'<p class="schedule-note">{t("ws_schedule_note", lang)}</p>', unsafe_allow_html=True)

    for day, sessions in days.items():
        with st.expander(f"{day}", expanded=(day == "Friday")):
            for time, theme, text, css_class in sessions:
                st.markdown(
                    f"""
                    <div class="compact-theme-row {css_class}">
                        <div>
                            <div class="theme-title">{theme}</div>
                            <div class="theme-text">{text}</div>
                        </div>
                        <div class="theme-time">🕒 {time}</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

with right:
    st.markdown(f"""
    <div class="side-card soft-card">
        <div class="side-icon">🚌</div>
        <div>
            <h3>Community Bus</h3>
            <p>The bus is currently at:</p>
            <strong>Chamberlain Gardens, Ladywood, Birmingham B16 8XN</strong>
            <br><br>
            <a href="bus?lang={lang}&text_size={st.session_state["text_size"]}" target="_self">
                Go to Bus page →
            </a>
        </div>
    </div>

    <div class="side-card soft-card">
        <div class="side-icon help-icon">🤝</div>
        <div>
            <h3>Need extra help?</h3>
            <p>Drop in for small questions. If you need support that we cannot assist with, please visit Civic Square.</p>
            <strong>
                Civic Square Birmingham CIC<br>
                Tubeworks, Canalside House<br>
                Rotton Park Street<br>
                Birmingham B16 0AF
            </strong>
        </div>
    </div>
    """, unsafe_allow_html=True)

### WORKSHOP REGISTRATION
with st.form("workshop_registration_form"):
    st.markdown(f'<div class="registration-title">{t("ws_register_title", lang)}</div>', unsafe_allow_html=True)
    st.markdown(
        f"""
        <div class="quick-note">
            <div class="quick-note-icon">📝</div>
            <div>
                <strong>Quick note</strong><br>
                {t("ws_quick_note", lang)}
            </div>
        </div>
        """,
        unsafe_allow_html=True)
    
    day_col, workshop_col = st.columns(2)
    with day_col:
        day = st.selectbox(
            t("ws_label_day_select", lang),
            [t("ws_select_a_day", lang), t("ws_option_day_monday", lang), t("ws_option_day_tuesday", lang), t("ws_option_day_wednesday", lang), t("ws_option_day_thursday", lang), t("ws_option_day_friday", lang), t("ws_option_day_saturday", lang), t("ws_option_day_sunday", lang)],
            key="ws_day_select",
        )

    with workshop_col:
        workshop_options = [
            t("ws_option_button", lang),
            t("ws_option_access", lang),
            t("ws_option_opportunity", lang),
            t("ws_option_confidence", lang),
        ]
        workshop = st.selectbox(
            t("ws_label_option_button", lang),
            workshop_options,
            key="ws_workshop_select",
        )



    col1, col2 = st.columns(2)

    with col1:
        first_name = st.text_input(t("ws_first_name",lang))

    with col2:
        last_name = st.text_input(t("ws_last_name", lang))

    phone = st.text_input(t("ws_phone", lang))
    notes = st.text_area(t("ws_notes", lang), height=120)

    submitted = st.form_submit_button(t("ws_submit",lang))

    if submitted:
        if workshop == t("ws_option_button", lang) or not first_name.strip() or not phone.strip():
            st.error(t("ws_error", lang))
        else:
            st.success(t("ws_success", lang))