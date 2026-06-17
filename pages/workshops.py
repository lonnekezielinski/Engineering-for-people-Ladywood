import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import streamlit as st
from translations import t
from styling import apply_style

# Page configuration
st.set_page_config(page_title="Workshops", layout="wide")

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

# Header
st.markdown(f'<div class="page-title">{t("ws_title", lang)}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="workshop-intro-box">{t("ws_subtitle", lang)}</div>', unsafe_allow_html=True)

# Workshop schedule
left, right = st.columns([2.2, 1])

days = {
    t("ws_option_day_monday", lang): [
        ("10:00 – 11:30", t("ws_access", lang), t("ws_mondayaccess", lang), "theme-access"),
        ("13:00 – 14:30 ", t("ws_opportunity", lang), t("ws_mondayopportunity", lang), "theme-opportunity"),
        ("15:00 – 16:30", t("ws_confidence", lang), t("ws_mondayconfidence", lang), "theme-confidence"),
    ],
    t("ws_option_day_tuesday", lang): [
        ("10:00 – 11:30", t("ws_access", lang), t("ws_tuesdayaccess", lang), "theme-access"),
        ("13:00 – 14:30", t("ws_opportunity", lang), t("ws_tuesdayopportunity", lang), "theme-opportunity"),
        ("15:00 – 16:30", t("ws_confidence", lang), t("ws_tuesdayconfidence", lang), "theme-confidence"),
    ],
    t("ws_option_day_wednesday", lang): [
        ("10:00 – 11:30", t("ws_access", lang), t("ws_wednesdayaccess", lang), "theme-access"),
        ("13:00 – 14:30", t("ws_opportunity", lang), t("ws_wednesdayopportunity", lang), "theme-opportunity"),
        ("15:00 – 16:30", t("ws_confidence", lang), t("ws_wednesdayconfidence", lang), "theme-confidence"),
    ],
    t("ws_option_day_thursday", lang): [
        ("10:00 – 11:30", t("ws_access", lang), t("ws_thursdayaccess", lang), "theme-access"),
        ("13:00 – 14:30", t("ws_opportunity", lang), t("ws_thursdayopportunity", lang), "theme-opportunity"),
        ("15:00 – 16:30", t("ws_confidence", lang), t("ws_thursdayconfidence", lang), "theme-confidence"),
    ],
    t("ws_option_day_friday", lang): [
        ("10:00 – 11:30", t("ws_access", lang), t("ws_fridayaccess", lang), "theme-access"),
        ("13:00 – 14:30", t("ws_opportunity", lang), t("ws_fridayopportunity", lang), "theme-opportunity"),
        ("15:00 – 16:30", t("ws_confidence", lang), t("ws_fridayconfidence", lang), "theme-confidence"),
    ],
    t("ws_option_day_saturday", lang): [
        ("10:00 – 11:30", t("ws_access", lang), t("ws_saturdayaccess", lang), "theme-access"),
        ("13:00 – 14:30", t("ws_opportunity", lang), t("ws_saturdayopportunity", lang), "theme-opportunity"),
        ("15:00 – 16:30", t("ws_confidence", lang), t("ws_saturdayconfidence", lang), "theme-confidence"),
    ],
    t("ws_option_day_sunday", lang): [
        ("10:00 – 11:30", t("ws_access", lang), t("ws_sundayaccess", lang), "theme-access"),
        ("13:00 – 14:30", t("ws_opportunity", lang), t("ws_sundayopportunity", lang), "theme-opportunity"),
        ("15:00 – 16:30", t("ws_confidence", lang), t("ws_sundayconfidence", lang), "theme-confidence"),
    ],
}

with left:
    st.markdown(f'<h2 class="schedule-main-title">{t("ws_schedule_title", lang)}</h2>', unsafe_allow_html=True)
    st.markdown(f'<p class="schedule-note">{t("ws_schedule_note", lang)}</p>', unsafe_allow_html=True)

    for day, sessions in days.items():
        with st.expander(day, expanded=False):
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
            <h3>{t("ws_communitybus", lang)}</h3>
            <p>{t("ws_communitybus", lang)}</p>
            <strong>Chamberlain Gardens, Ladywood, Birmingham B16 8XN</strong>
            <br><br>
            <a href="bus?lang={lang}&text_size={st.session_state["text_size"]}" target="_self">
                {t("ws_go_to_bus_page", lang)}
            </a>
        </div>
    </div>

    <div class="side-card soft-card">
        <div class="side-icon help-icon">🤝</div>
        <div>
            <h3>{t("ws_need_extra_help", lang)}</h3>
            <p>{t("ws_need_extra_help_text", lang)}</p>
            <strong>
                Civic Square Birmingham CIC<br>
                Tubeworks, Canalside House<br>
                Rotton Park Street<br>
                Birmingham B16 0AF
            </strong>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Workshop registration
with st.form("workshop_registration_form"):
    st.markdown(f'<div class="registration-title">{t("ws_register_title", lang)}</div>', unsafe_allow_html=True)
    st.markdown(
        f"""
        <div class="quick-note">
            <div class="quick-note-icon">📝</div>
            <div>
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