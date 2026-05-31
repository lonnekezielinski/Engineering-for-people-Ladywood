import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import streamlit as st
import tempfile
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

if "text_size" not in st.session_state:
    st.session_state["text_size"] = "A"

text_size = st.session_state["text_size"]

if text_size == "A":
    page_title_size = "58px"
    body_size = "18px"
    form_title_size = "1.8rem"
elif text_size == "A+":
    page_title_size = "70px"
    body_size = "22px"
    form_title_size = "2.2rem"
else:
    page_title_size = "82px"
    body_size = "26px"
    form_title_size = "2.6rem"

def show_html_as_iframe(html_content, height=820):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".html", mode="w", encoding="utf-8") as f:
        f.write(html_content)
        file_path = f.name
    st.iframe(file_path, height=height)

### CUSTOM CSS
st.markdown(f"""
<style>
    [data-testid="stAppViewContainer"] {{background-color: #F5F2EA;}}
    [data-testid="stHeader"] {{background-color: transparent;}}
    .block-container {{padding-top: 1rem;}}
    #MainMenu, footer {{visibility: hidden;}}
    [data-testid="stSidebar"] {{ display:none; }}

    .form-section {{ background:white; border:2px solid rgba(0,0,0,0.06); border-radius:28px; padding:2rem 2.5rem; max-width:650px; margin:0 auto 3rem auto; box-shadow:0 4px 12px rgba(0,0,0,0.04); }}
    .form-title    {{ font-family:'Playfair Display',serif; font-size:1.8rem; font-weight:900; color:#1a1a1a; margin-bottom:0.3rem; }}
    .form-subtitle {{ font-size:0.9rem; color:#888; margin-bottom:2rem; }}

    div[data-testid="stTextInput"] input {{ border-radius:50px !important; border:1.5px solid #e5e5e5 !important; padding:0.65rem 1.2rem !important; font-size:0.95rem !important; background:#fafafa !important; }}
    div[data-testid="stTextInput"] input:focus {{ border-color:#f7679a !important; background:white !important; box-shadow:0 0 0 3px rgba(247,103,154,0.1) !important; }}
    div[data-testid="stTextInput"] label {{ font-size:0.85rem !important; font-weight:500 !important; color:#444 !important; }}

    div[data-testid="stForm"] button[type="submit"] {{ background:#285C7A !important; color:white !important; border:none !important; border-radius:50px !important; padding:0.75rem 2rem !important; font-size:0.95rem !important; font-weight:500 !important; width:100% !important; cursor:pointer !important; margin-top:0.5rem !important; }}
    div[data-testid="stForm"] button[type="submit"]:hover {{ background:#333 !important; }}

    .success-box  {{ background:#e8f5e9; border-radius:16px; padding:1.5rem 2rem; text-align:center; max-width:560px; margin:0 auto 3rem auto; }}
    .success-icon  {{ font-size:2.5rem; margin-bottom:0.5rem; }}
    .success-title {{ font-size:1.2rem; font-weight:700; color:#2e7d32; margin-bottom:0.3rem; }}
    .success-text  {{ font-size:0.9rem; color:#555; }}

    .privacy-notice       {{ background:#f0f4ff; border-left:4px solid #c4b5e8; border-radius:12px; padding:1rem 1.2rem; margin-top:1rem; }}
    .privacy-notice-title {{ font-size:0.82rem; font-weight:700; color:#5a4a7a; margin-bottom:0.4rem; }}
    .privacy-notice p     {{ font-size:0.78rem; color:#666; line-height:1.6; margin:0.2rem 0; }}
    .privacy-notice ul    {{ font-size:0.78rem; color:#666; line-height:1.7; margin:0.3rem 0 0 0; padding-left:1.2rem; }}

    .stButton > button {{ background:white; border-radius:18px; border:2px solid #D8D2C7; padding:12px 18px; font-size:18px; color:#444; margin-bottom:25px; }}
    .intro-box {{ background:#C8E2F5; border:2px solid #9CC7E6; border-radius:24px; padding:22px 28px; margin-bottom:30px; font-size:19px; color:#285C7A; line-height:1.5; }}

    .page-title {{ font-size:{page_title_size}; font-weight:900; color:#0D1B3D; margin-bottom:10px; }}
    .intro-box {{ background:#C8E2F5; border:2px solid #9CC7E6; border-radius:24px; padding:22px 28px; margin-bottom:30px; font-size:{body_size}; color:#285C7A; line-height:1.5; }}
    .form-title {{ font-family:'Playfair Display',serif; font-size:{form_title_size}; font-weight:900; color:#1a1a1a; margin-bottom:0.3rem; }}
    .form-subtitle {{ font-size:{body_size}; color:#888; margin-bottom:2rem; }}
    .setting-label {{ font-size:{body_size}; font-weight:700; color:#0D1B3D; margin-bottom:8px; }}
    [data-testid="stSelectbox"] {{ width:280px !important; max-width:280px; }}
    [data-testid="stRadio"] {{ width:240px !important; background:white; border:2px solid #D8D2C7; border-radius:18px; padding:6px 12px; }}
    div[role="radiogroup"] label p {{ color:#0D1B3D !important; font-weight:600 !important;}}
    [data-baseweb="select"] > div {{ background-color:white !important; border:2px solid #D8D2C7 !important; border-radius:18px !important; color:#222 !important; }}
    [data-baseweb="select"] span {{ color:#222 !important; font-weight:500; }}
</style>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

st.markdown(apply_rtl_css(lang), unsafe_allow_html=True)

### TOP BAR
top_left, spacer, top_right = st.columns([2, 0.3, 1.7])

with top_left:
    if st.button(t("ws_back", lang)):
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
            ["A", "A+", "A++"],
            index=["A", "A+", "A++"].index(st.session_state["text_size"]),
            horizontal=True,
            label_visibility="collapsed",
            key="ws_text_size_radio"
        )

        if text_size != st.session_state["text_size"]:
            st.session_state["text_size"] = text_size
            st.rerun()

### HEADER
st.markdown(f'<div class="page-title">{t("ws_title", lang)}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="intro-box">{t("ws_subtitle", lang)}</div>', unsafe_allow_html=True)

### CARDS IFRAME
cards_html = """<!DOCTYPE html>
<html><head>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">
<style>
body{margin:0;padding:1rem 0;background-color:#fdf6f0;font-family:'DM Sans',sans-serif;}
.top-bar{display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:3rem;}
.top-bar-stats{display:flex;gap:1.5rem;}
.stat-badge{display:flex;align-items:center;gap:0.6rem;background:white;border-radius:50px;padding:0.5rem 1.1rem;box-shadow:0 2px 12px rgba(0,0,0,0.07);}
.stat-icon{font-size:1.4rem;}.stat-value{font-size:1.05rem;font-weight:600;color:#1a1a1a;}.stat-label{font-size:0.72rem;color:#999;}
.cards-row{display:flex;gap:1.1rem;align-items:flex-end;margin-bottom:3rem;overflow-x:auto;}
a.card-link{text-decoration:none;display:flex;flex:1;min-width:170px;max-width:240px;}
.workshop-card{flex:1;border-radius:130px 130px 110px 110px;padding:1.4rem 1.2rem 1.6rem;cursor:pointer;transition:transform 0.3s ease,box-shadow 0.3s ease;display:flex;flex-direction:column;align-items:center;text-align:center;}
.workshop-card:hover{transform:translateY(-8px);box-shadow:0 18px 40px rgba(0,0,0,0.13);}
.card-tall{min-height:380px;}.card-medium{min-height:340px;margin-bottom:40px;}.card-tall2{min-height:400px;}.card-medium2{min-height:330px;margin-bottom:55px;}.card-short{min-height:310px;margin-bottom:20px;}
.card-pink{background:#f7679a;}.card-sage{background:#c8d5b9;}.card-amber{background:#f7c45e;}.card-lavender{background:#c4b5e8;}.card-mint{background:#a8d8a0;}
.card-icon-wrap{width:110px;height:110px;border-radius:50%;background:rgba(255,255,255,0.35);margin-bottom:1rem;border:3px solid rgba(255,255,255,0.6);display:flex;align-items:center;justify-content:center;font-size:2.8rem;}
.card-bottom{margin-top:auto;}.card-title{font-size:0.95rem;font-weight:600;color:rgba(0,0,0,0.75);margin-bottom:0.4rem;}
.card-arrow{display:inline-block;width:30px;height:30px;background:rgba(255,255,255,0.45);border-radius:50%;line-height:30px;font-size:1rem;color:rgba(0,0,0,0.65);}
.hero-row{display:flex;justify-content:space-between;align-items:flex-end;gap:2rem;flex-wrap:wrap;}
.hero-headline{font-family:'Playfair Display',serif;font-size:clamp(2.4rem,4vw,3.8rem);font-weight:900;color:#1a1a1a;line-height:1.08;margin:0;}
.hero-right{display:flex;flex-direction:column;align-items:flex-end;gap:1rem;}
.participants{display:flex;align-items:center;gap:0.7rem;}
.avatar-stack{display:flex;}.avatar{width:32px;height:32px;border-radius:50%;border:2px solid #fdf6f0;margin-left:-10px;font-size:1.1rem;display:flex;align-items:center;justify-content:center;}
.avatar:first-child{margin-left:0;}.participants-text{font-size:0.82rem;color:#888;}.participants-text strong{color:#1a1a1a;}
.cta-buttons{display:flex;gap:0.8rem;}.cta-buttons a{text-decoration:none;}
.btn-secondary{background:transparent;color:#1a1a1a;border:2px solid #1a1a1a;border-radius:50px;padding:0.7rem 1.5rem;font-family:'DM Sans',sans-serif;font-size:0.88rem;font-weight:500;cursor:pointer;}
</style></head><body>
<div class="top-bar"><div class="top-bar-stats">
<div class="stat-badge"><span class="stat-icon">⭐</span><div><div class="stat-value">4.9</div><div class="stat-label">Rating</div></div></div>
<div class="stat-badge"><span class="stat-icon">🏅</span><div><div class="stat-value">Certified</div><div class="stat-label">Facilitators</div></div></div>
</div></div>
<div class="cards-row">
<a class="card-link" href="https://www.saathihouse.org/projects" target="_blank"><div class="workshop-card card-pink card-tall"><div class="card-icon-wrap">🗣️</div><div class="card-bottom"><div class="card-title">Language Bridges</div><div class="card-arrow">→</div></div></div></a>
<a class="card-link" href="https://digitalnns.org.uk" target="_blank"><div class="workshop-card card-sage card-medium"><div class="card-icon-wrap">💻</div><div class="card-bottom"><div class="card-title">Digital Inclusion</div><div class="card-arrow">→</div></div></div></a>
<a class="card-link" href="https://digitalnns.org.uk/first-fact-or-fiction-session/" target="_blank"><div class="workshop-card card-amber card-tall2"><div class="card-icon-wrap">🔒</div><div class="card-bottom"><div class="card-title">Online Safety</div><div class="card-arrow">→</div></div></div></a>
<a class="card-link" href="https://www.birminghamsettlement.org.uk/ladywood/" target="_blank"><div class="workshop-card card-lavender card-medium2"><div class="card-icon-wrap">📱</div><div class="card-bottom"><div class="card-title">Everyday Tech</div><div class="card-arrow">→</div></div></div></a>
<a class="card-link" href="https://www.birminghamsettlement.org.uk/neighbourhood-futures-festival/" target="_blank"><div class="workshop-card card-mint card-short"><div class="card-icon-wrap">🤝</div><div class="card-bottom"><div class="card-title">Community Connect</div><div class="card-arrow">→</div></div></div></a>
</div>
<div class="hero-row">
<h1 class="hero-headline">Skills That Open<br>Doors for Everyone</h1>
<div class="hero-right">
<div class="participants"><div class="avatar-stack"><div class="avatar">👩</div><div class="avatar">👨</div><div class="avatar">👩</div><div class="avatar">🧑</div></div><div class="participants-text"><strong>2.4K+</strong><br>Participants Joined</div></div>
<div class="cta-buttons"><a href="https://digitalnns.org.uk/news-and-events/" target="_blank"><button class="btn-secondary">Browse All</button></a></div>
</div></div>
</body></html>"""

show_html_as_iframe(cards_html, height=820)

# ── Registration Form ──
if "registered" not in st.session_state:
    st.session_state.registered = False

if st.session_state.registered:
    name = st.session_state.get("reg_name", "")
    st.markdown(f"""
    <div class="success-box">
        <div class="success-icon">🎉</div>
        <div class="success-title">{t("ws_success_title", lang).format(name=name)}</div>
        <div class="success-text">{t("ws_success_text", lang)}</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button(t("ws_register_another", lang)):
        st.session_state.registered = False
        st.rerun()
else:
    st.markdown(f"""
    <div class="form-section">
        <div class="form-title">{t("ws_register_title", lang)}</div>
        <div class="form-subtitle">{t("ws_register_sub", lang)}</div>
    </div>
    """, unsafe_allow_html=True)

    with st.form("registration_form"):
        col1, col2 = st.columns(2)
        with col1:
            first_name = st.text_input(t("ws_first_name", lang))
        with col2:
            last_name = st.text_input(t("ws_last_name", lang))
        phone = st.text_input(t("ws_phone", lang))
        email = st.text_input(t("ws_email", lang))

        st.markdown("""
        <div class="privacy-notice">
            <div class="privacy-notice-title">🔒 Your Privacy Matters</div>
            <p>We only collect the information you share here.</p>
            <ul>
                <li><strong>Name & phone number</strong> — used only to confirm your place.</li>
                <li><strong>Email</strong> — optional, used only for reminders.</li>
                <li>Your details are <strong>never shared</strong> with third parties.</li>
                <li>You can ask us to <strong>delete your details</strong> at any time.</li>
            </ul>
            <p style="margin-top:0.5rem;color:#888;">This service follows GDPR principles.</p>
        </div>
        """, unsafe_allow_html=True)

        submitted = st.form_submit_button(t("ws_submit", lang))
        if submitted:
            if not first_name.strip() or not last_name.strip() or not phone.strip():
                st.error(t("ws_error", lang))
            else:
                st.session_state.registered = True
                st.session_state.reg_name = first_name.strip()
                st.rerun()

st.markdown("---")

print_html = """<!DOCTYPE html><html><head>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">
<style>
body{margin:0;padding:1.5rem 2rem;background:white;font-family:'DM Sans',sans-serif;color:#1a1a1a;}
.print-btn{background:#1a1a1a;color:white;border:none;border-radius:50px;padding:0.65rem 1.6rem;font-size:0.9rem;font-weight:500;cursor:pointer;margin-bottom:1.5rem;}
.flyer{border:2px solid #1a1a1a;border-radius:16px;padding:2rem 2.5rem;max-width:720px;}
.flyer-header{display:flex;justify-content:space-between;align-items:flex-start;border-bottom:2px solid #1a1a1a;padding-bottom:1rem;margin-bottom:1.5rem;}
.flyer-title{font-family:'Playfair Display',serif;font-size:2rem;font-weight:900;line-height:1.1;margin:0;}
.flyer-title span{color:#f7679a;}
.flyer-meta{text-align:right;font-size:0.8rem;color:#555;line-height:1.7;}
.flyer-tagline{font-size:0.95rem;color:#555;margin-bottom:1.5rem;line-height:1.6;}
.workshops-grid{display:grid;grid-template-columns:1fr 1fr;gap:0.8rem;margin-bottom:1.5rem;}
.workshop-item{border:1.5px solid #e5e5e5;border-radius:12px;padding:0.8rem 1rem;display:flex;align-items:flex-start;gap:0.7rem;}
.dot{width:10px;height:10px;border-radius:50%;display:inline-block;flex-shrink:0;margin-top:4px;}
.dot-pink{background:#f7679a;}.dot-sage{background:#c8d5b9;}.dot-amber{background:#f7c45e;}.dot-lavender{background:#c4b5e8;}.dot-mint{background:#a8d8a0;}
.w-name{font-weight:700;font-size:0.88rem;margin-bottom:0.15rem;}.w-org{font-size:0.75rem;color:#888;}
.reg-strip{background:#1a1a1a;color:white;border-radius:12px;padding:1rem 1.5rem;display:flex;justify-content:space-between;align-items:center;margin-bottom:1.2rem;flex-wrap:wrap;gap:1rem;}
.reg-strip-left{font-size:0.95rem;font-weight:600;}.reg-strip-sub{font-size:0.75rem;color:#aaa;margin-top:0.15rem;}
.reg-fields{display:flex;gap:1rem;flex-wrap:wrap;}
.reg-field-label{font-size:0.65rem;color:#aaa;margin-bottom:0.2rem;}.reg-field-line{border-bottom:1px solid #555;width:110px;height:16px;}
.privacy{border:1px solid #c4b5e8;border-radius:10px;padding:0.8rem 1rem;font-size:0.72rem;color:#555;line-height:1.6;background:#f8f5ff;}
.flyer-footer{border-top:1px solid #e5e5e5;margin-top:1.2rem;padding-top:0.8rem;font-size:0.72rem;color:#aaa;text-align:center;}
@media print{.print-btn{display:none!important;}}
</style></head><body>
<button class="print-btn" onclick="window.print()">🖨️ Print / Save as PDF</button>
<div class="flyer">
<div class="flyer-header"><h1 class="flyer-title">Community<br><span>Workshops</span></h1><div class="flyer-meta"><strong>Ladywood, Birmingham</strong><br>Free to attend<br>No account needed<br>All skill levels welcome</div></div>
<p class="flyer-tagline">Build confidence with language, technology, and digital skills. All workshops are free, beginner-friendly, and open to everyone.</p>
<div class="workshops-grid">
<div class="workshop-item"><span class="dot dot-pink"></span><div><div class="w-name">🗣️ Language Bridges</div><div class="w-org">Saathi House</div></div></div>
<div class="workshop-item"><span class="dot dot-sage"></span><div><div class="w-name">💻 Digital Inclusion</div><div class="w-org">Digital NNS</div></div></div>
<div class="workshop-item"><span class="dot dot-amber"></span><div><div class="w-name">🔒 Online Safety</div><div class="w-org">Digital NNS</div></div></div>
<div class="workshop-item"><span class="dot dot-lavender"></span><div><div class="w-name">📱 Everyday Tech</div><div class="w-org">Birmingham Settlement</div></div></div>
<div class="workshop-item"><span class="dot dot-mint"></span><div><div class="w-name">🤝 Community Connect</div><div class="w-org">Birmingham Settlement</div></div></div>
</div>
<div class="reg-strip"><div><div class="reg-strip-left">Register here — no account needed</div><div class="reg-strip-sub">Fill in your details or speak to a member of staff</div></div>
<div class="reg-fields">
<div><div class="reg-field-label">FIRST NAME</div><div class="reg-field-line"></div></div>
<div><div class="reg-field-label">LAST NAME</div><div class="reg-field-line"></div></div>
<div><div class="reg-field-label">PHONE NUMBER</div><div class="reg-field-line"></div></div>
<div><div class="reg-field-label">EMAIL (OPTIONAL)</div><div class="reg-field-line"></div></div>
</div></div>
<div class="privacy"><strong>🔒 Your Privacy (GDPR)</strong> — We only collect what you write here. Never shared with third parties.</div>
<div class="flyer-footer">Digital Inclusion Community Support System | Ladywood, Birmingham | Free & Open to All</div>
</div></body></html>"""
show_html_as_iframe(print_html, height=820)