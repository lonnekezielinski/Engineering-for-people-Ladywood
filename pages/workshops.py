import streamlit as st
import streamlit.components.v1 as components
st.title("Workshops")

st.set_page_config(page_title="Workshops", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #fdf6f0; }
    [data-testid="stAppViewContainer"] { background-color: #fdf6f0; }
    [data-testid="stHeader"] { background-color: #fdf6f0; }
    #MainMenu, footer, header { visibility: hidden; }

    /* Form container */
    .form-section {
        background: white;
        border-radius: 24px;
        padding: 2.5rem 3rem;
        max-width: 560px;
        margin: 0 auto 3rem auto;
        box-shadow: 0 4px 30px rgba(0,0,0,0.08);
    }
    .form-title {
        font-family: 'Playfair Display', serif;
        font-size: 1.8rem;
        font-weight: 900;
        color: #1a1a1a;
        margin-bottom: 0.3rem;
    }
    .form-subtitle {
        font-size: 0.9rem;
        color: #888;
        margin-bottom: 2rem;
    }

    /* Style Streamlit inputs */
    div[data-testid="stTextInput"] input {
        border-radius: 50px !important;
        border: 1.5px solid #e5e5e5 !important;
        padding: 0.65rem 1.2rem !important;
        font-family: 'DM Sans', sans-serif !important;
        font-size: 0.95rem !important;
        background: #fafafa !important;
        transition: border 0.2s !important;
    }
    div[data-testid="stTextInput"] input:focus {
        border-color: #f7679a !important;
        background: white !important;
        box-shadow: 0 0 0 3px rgba(247,103,154,0.1) !important;
    }
    div[data-testid="stTextInput"] label {
        font-family: 'DM Sans', sans-serif !important;
        font-size: 0.85rem !important;
        font-weight: 500 !important;
        color: #444 !important;
    }

    /* Submit button */
    div[data-testid="stForm"] button[type="submit"] {
        background: #1a1a1a !important;
        color: white !important;
        border: none !important;
        border-radius: 50px !important;
        padding: 0.75rem 2rem !important;
        font-family: 'DM Sans', sans-serif !important;
        font-size: 0.95rem !important;
        font-weight: 500 !important;
        width: 100% !important;
        cursor: pointer !important;
        transition: background 0.2s !important;
        margin-top: 0.5rem !important;
    }
    div[data-testid="stForm"] button[type="submit"]:hover {
        background: #333 !important;
    }

    /* Success box */
    .success-box {
        background: #e8f5e9;
        border-radius: 16px;
        padding: 1.5rem 2rem;
        text-align: center;
        max-width: 560px;
        margin: 0 auto 3rem auto;
    }
    .success-icon { font-size: 2.5rem; margin-bottom: 0.5rem; }
    .success-title { font-size: 1.2rem; font-weight: 700; color: #2e7d32; margin-bottom: 0.3rem; }
    .success-text { font-size: 0.9rem; color: #555; }

    /* Privacy notice */
    .privacy-notice {
        background: #f0f4ff;
        border-left: 4px solid #c4b5e8;
        border-radius: 12px;
        padding: 1rem 1.2rem;
        margin-top: 1rem;
        font-family: 'DM Sans', sans-serif;
    }
    .privacy-notice-title {
        font-size: 0.82rem;
        font-weight: 700;
        color: #5a4a7a;
        margin-bottom: 0.4rem;
    }
    .privacy-notice p {
        font-size: 0.78rem;
        color: #666;
        line-height: 1.6;
        margin: 0.2rem 0;
    }
    .privacy-notice ul {
        font-size: 0.78rem;
        color: #666;
        line-height: 1.7;
        margin: 0.3rem 0 0 0;
        padding-left: 1.2rem;
    }

    /* Divider */
    .divider {
        text-align: center;
        font-size: 0.85rem;
        color: #aaa;
        margin: 0.5rem 0 2rem 0;
        font-family: 'DM Sans', sans-serif;
    }
</style>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)


cards_html = """
<!DOCTYPE html>
<html>
<head>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">
<style>
    body { margin: 0; padding: 1rem 0; background-color: #fdf6f0; font-family: 'DM Sans', sans-serif; }

    .top-bar { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 3rem; }
    .top-bar-subtitle { max-width: 380px; font-size: 1rem; color: #6b6b6b; line-height: 1.6; }
    .top-bar-stats { display: flex; gap: 1.5rem; }
    .stat-badge { display: flex; align-items: center; gap: 0.6rem; background: white; border-radius: 50px; padding: 0.5rem 1.1rem; box-shadow: 0 2px 12px rgba(0,0,0,0.07); }
    .stat-icon { font-size: 1.4rem; }
    .stat-value { font-size: 1.05rem; font-weight: 600; color: #1a1a1a; }
    .stat-label { font-size: 0.72rem; color: #999; }

    .cards-row { display: flex; gap: 1.1rem; align-items: flex-end; margin-bottom: 3rem; overflow-x: auto; }

    a.card-link { text-decoration: none; display: flex; flex: 1; min-width: 170px; max-width: 240px; }
    .workshop-card { flex: 1; border-radius: 130px 130px 110px 110px; padding: 1.4rem 1.2rem 1.6rem; cursor: pointer; transition: transform 0.3s ease, box-shadow 0.3s ease; display: flex; flex-direction: column; align-items: center; text-align: center; }
    .workshop-card:hover { transform: translateY(-8px); box-shadow: 0 18px 40px rgba(0,0,0,0.13); }

    .card-tall    { min-height: 380px; }
    .card-medium  { min-height: 340px; margin-bottom: 40px; }
    .card-tall2   { min-height: 400px; }
    .card-medium2 { min-height: 330px; margin-bottom: 55px; }
    .card-short   { min-height: 310px; margin-bottom: 20px; }

    .card-pink     { background: #f7679a; }
    .card-sage     { background: #c8d5b9; }
    .card-amber    { background: #f7c45e; }
    .card-lavender { background: #c4b5e8; }
    .card-mint     { background: #a8d8a0; }

    .card-icon-wrap { width: 110px; height: 110px; border-radius: 50%; background: rgba(255,255,255,0.35); margin-bottom: 1rem; border: 3px solid rgba(255,255,255,0.6); display: flex; align-items: center; justify-content: center; font-size: 2.8rem; }
    .card-bottom { margin-top: auto; }
    .card-title { font-size: 0.95rem; font-weight: 600; color: rgba(0,0,0,0.75); margin-bottom: 0.4rem; }
    .card-arrow { display: inline-block; width: 30px; height: 30px; background: rgba(255,255,255,0.45); border-radius: 50%; line-height: 30px; font-size: 1rem; color: rgba(0,0,0,0.65); }

    .hero-row { display: flex; justify-content: space-between; align-items: flex-end; gap: 2rem; flex-wrap: wrap; }
    .hero-headline { font-family: 'Playfair Display', serif; font-size: clamp(2.4rem, 4vw, 3.8rem); font-weight: 900; color: #1a1a1a; line-height: 1.08; margin: 0; }
    .hero-right { display: flex; flex-direction: column; align-items: flex-end; gap: 1rem; }
    .participants { display: flex; align-items: center; gap: 0.7rem; }
    .avatar-stack { display: flex; }
    .avatar { width: 32px; height: 32px; border-radius: 50%; border: 2px solid #fdf6f0; margin-left: -10px; font-size: 1.1rem; display: flex; align-items: center; justify-content: center; }
    .avatar:first-child { margin-left: 0; }
    .participants-text { font-size: 0.82rem; color: #888; }
    .participants-text strong { color: #1a1a1a; }
    .cta-buttons { display: flex; gap: 0.8rem; }
    .cta-buttons a { text-decoration: none; }
    .btn-primary { background: #1a1a1a; color: white; border: none; border-radius: 50px; padding: 0.7rem 1.5rem; font-family: 'DM Sans', sans-serif; font-size: 0.88rem; font-weight: 500; cursor: pointer; }
    .btn-secondary { background: transparent; color: #1a1a1a; border: 2px solid #1a1a1a; border-radius: 50px; padding: 0.7rem 1.5rem; font-family: 'DM Sans', sans-serif; font-size: 0.88rem; font-weight: 500; cursor: pointer; }
</style>
</head>
<body>

<div class="top-bar">
    <p class="top-bar-subtitle">Community workshops and digital support sessions.</p>
    <div class="top-bar-stats">
        <div class="stat-badge">
            <span class="stat-icon">&#11088;</span>
            <div><div class="stat-value">4.9</div><div class="stat-label">Rating</div></div>
        </div>
        <div class="stat-badge">
            <span class="stat-icon">&#127945;</span>
            <div><div class="stat-value">Certified</div><div class="stat-label">Facilitators</div></div>
        </div>
    </div>
</div>

<div class="cards-row">
    <a class="card-link" href="https://www.saathihouse.org/projects" target="_blank">
        <div class="workshop-card card-pink card-tall">
            <div class="card-icon-wrap">&#128483;</div>
            <div class="card-bottom"><div class="card-title">Language Bridges</div><div class="card-arrow">&#8594;</div></div>
        </div>
    </a>
    <a class="card-link" href="https://digitalnns.org.uk" target="_blank">
        <div class="workshop-card card-sage card-medium">
            <div class="card-icon-wrap">&#128187;</div>
            <div class="card-bottom"><div class="card-title">Digital Inclusion</div><div class="card-arrow">&#8594;</div></div>
        </div>
    </a>
    <a class="card-link" href="https://digitalnns.org.uk/first-fact-or-fiction-session/" target="_blank">
        <div class="workshop-card card-amber card-tall2">
            <div class="card-icon-wrap">&#128274;</div>
            <div class="card-bottom"><div class="card-title">Online Safety</div><div class="card-arrow">&#8594;</div></div>
        </div>
    </a>
    <a class="card-link" href="https://www.birminghamsettlement.org.uk/ladywood/" target="_blank">
        <div class="workshop-card card-lavender card-medium2">
            <div class="card-icon-wrap">&#128241;</div>
            <div class="card-bottom"><div class="card-title">Everyday Tech</div><div class="card-arrow">&#8594;</div></div>
        </div>
    </a>
    <a class="card-link" href="https://www.birminghamsettlement.org.uk/neighbourhood-futures-festival/" target="_blank">
        <div class="workshop-card card-mint card-short">
            <div class="card-icon-wrap">&#129309;</div>
            <div class="card-bottom"><div class="card-title">Community Connect</div><div class="card-arrow">&#8594;</div></div>
        </div>
    </a>
</div>

<div class="hero-row">
    <h1 class="hero-headline">Skills That Open<br>Doors for Everyone</h1>
    <div class="hero-right">
        <div class="participants">
            <div class="avatar-stack">
                <div class="avatar">&#128105;</div>
                <div class="avatar">&#128104;</div>
                <div class="avatar">&#128105;</div>
                <div class="avatar">&#129489;</div>
            </div>
            <div class="participants-text"><strong>2.4K+</strong><br>Participants Joined</div>
        </div>
        <div class="cta-buttons">
            <a href="https://digitalnns.org.uk/news-and-events/" target="_blank"><button class="btn-secondary">Browse All</button></a>
        </div>
    </div>
</div>

</body>
</html>
"""

components.html(cards_html, height=820, scrolling=False)

# ── Divider ──
st.markdown('<div class="divider">── Register below — no account needed ──</div>', unsafe_allow_html=True)

# ── Registration Form ──
if "registered" not in st.session_state:
    st.session_state.registered = False

if st.session_state.registered:
    name = st.session_state.get("reg_name", "")
    st.markdown(f"""
    <div class="success-box">
        <div class="success-icon">&#127881;</div>
        <div class="success-title">You're registered, {name}!</div>
        <div class="success-text">We'll be in touch soon. See you at the workshop!</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Register another person"):
        st.session_state.registered = False
        st.rerun()
else:
    st.markdown("""
    <div class="form-section">
        <div class="form-title">Register Now</div>
        <div class="form-subtitle">Free to join &nbsp;·&nbsp; No account needed</div>
    </div>
    """, unsafe_allow_html=True)

    with st.form("registration_form"):
        col1, col2 = st.columns(2)
        with col1:
            first_name = st.text_input("First Name *")
        with col2:
            last_name = st.text_input("Last Name *")

        phone = st.text_input("Phone Number *")
        email = st.text_input("Email (optional)")

        st.markdown("""
        <div class="privacy-notice">
            <div class="privacy-notice-title">&#128274;&nbsp; Your Privacy Matters</div>
            <p>We only collect the information you share here. Here is what we do with it:</p>
            <ul>
                <li><strong>Name &amp; phone number</strong> — used only to confirm your place and contact you if anything changes.</li>
                <li><strong>Email</strong> — optional. Only used to send workshop reminders if you choose to share it.</li>
                <li>Your details are <strong>never shared</strong> with third parties or used for marketing.</li>
                <li>You can ask us to <strong>delete your details</strong> at any time by speaking to a member of staff.</li>
            </ul>
            <p style="margin-top:0.5rem; color:#888;">This service follows GDPR principles. We only collect what is necessary.</p>
        </div>
        """, unsafe_allow_html=True)

        submitted = st.form_submit_button("Register →")

        if submitted:
            if not first_name.strip() or not last_name.strip() or not phone.strip():
                st.error("Please fill in your first name, last name, and phone number.")
            else:
                st.session_state.registered = True
                st.session_state.reg_name = first_name.strip()
                st.rerun()
# ── Print-friendly flyer ──
st.markdown("---")

print_html = """
<!DOCTYPE html>
<html>
<head>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">
<style>
    body { margin: 0; padding: 1.5rem 2rem; background: white; font-family: 'DM Sans', sans-serif; color: #1a1a1a; }

    .print-btn { background: #1a1a1a; color: white; border: none; border-radius: 50px; padding: 0.65rem 1.6rem; font-family: 'DM Sans', sans-serif; font-size: 0.9rem; font-weight: 500; cursor: pointer; margin-bottom: 1.5rem; display: flex; align-items: center; gap: 0.5rem; }
    .print-btn:hover { background: #333; }

    .flyer { border: 2px solid #1a1a1a; border-radius: 16px; padding: 2rem 2.5rem; max-width: 720px; }

    .flyer-header { display: flex; justify-content: space-between; align-items: flex-start; border-bottom: 2px solid #1a1a1a; padding-bottom: 1rem; margin-bottom: 1.5rem; }
    .flyer-title { font-family: 'Playfair Display', serif; font-size: 2rem; font-weight: 900; line-height: 1.1; margin: 0; }
    .flyer-title span { color: #f7679a; }
    .flyer-meta { text-align: right; font-size: 0.8rem; color: #555; line-height: 1.7; }
    .flyer-meta strong { color: #1a1a1a; font-size: 0.85rem; }

    .flyer-tagline { font-size: 0.95rem; color: #555; margin-bottom: 1.5rem; line-height: 1.6; }

    .workshops-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 0.8rem; margin-bottom: 1.5rem; }
    .workshop-item { border: 1.5px solid #e5e5e5; border-radius: 12px; padding: 0.8rem 1rem; display: flex; align-items: flex-start; gap: 0.7rem; }
    .dot { width: 10px; height: 10px; border-radius: 50%; display: inline-block; flex-shrink: 0; margin-top: 4px; }
    .dot-pink { background: #f7679a; } .dot-sage { background: #c8d5b9; }
    .dot-amber { background: #f7c45e; } .dot-lavender { background: #c4b5e8; } .dot-mint { background: #a8d8a0; }
    .w-name { font-weight: 700; font-size: 0.88rem; margin-bottom: 0.15rem; }
    .w-org  { font-size: 0.75rem; color: #888; }
    .w-url  { font-size: 0.7rem; color: #f7679a; word-break: break-all; }

    .reg-strip { background: #1a1a1a; color: white; border-radius: 12px; padding: 1rem 1.5rem; display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.2rem; flex-wrap: wrap; gap: 1rem; }
    .reg-strip-left { font-size: 0.95rem; font-weight: 600; }
    .reg-strip-sub { font-size: 0.75rem; color: #aaa; margin-top: 0.15rem; }
    .reg-fields { display: flex; gap: 1rem; flex-wrap: wrap; }
    .reg-field-label { font-size: 0.65rem; color: #aaa; margin-bottom: 0.2rem; }
    .reg-field-line { border-bottom: 1px solid #555; width: 110px; height: 16px; }

    .privacy { border: 1px solid #c4b5e8; border-radius: 10px; padding: 0.8rem 1rem; font-size: 0.72rem; color: #555; line-height: 1.6; background: #f8f5ff; }
    .privacy strong { color: #5a4a7a; }

    .flyer-footer { border-top: 1px solid #e5e5e5; margin-top: 1.2rem; padding-top: 0.8rem; font-size: 0.72rem; color: #aaa; text-align: center; }

    @media print {
        body { padding: 0; }
        .print-btn { display: none !important; }
        .flyer { border-radius: 0; border: none; padding: 0; max-width: 100%; }
        .reg-strip { background: #1a1a1a !important; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
        .privacy { background: #f8f5ff !important; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
        .dot { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
    }
</style>
</head>
<body>

<button class="print-btn" onclick="window.print()">&#128438;&nbsp; Print / Save as PDF</button>

<div class="flyer">
    <div class="flyer-header">
        <h1 class="flyer-title">Community<br><span>Workshops</span></h1>
        <div class="flyer-meta">
            <strong>Ladywood, Birmingham</strong><br>
            Free to attend<br>
            No account needed<br>
            All skill levels welcome
        </div>
    </div>

    <p class="flyer-tagline">Build confidence with language, technology, and digital skills. All workshops are free, beginner-friendly, and open to everyone in the community.</p>

    <div class="workshops-grid">
        <div class="workshop-item">
            <span class="dot dot-pink"></span>
            <div><div class="w-name">&#128483; Language Bridges</div><div class="w-org">Saathi House</div><div class="w-url">saathihouse.org/projects</div></div>
        </div>
        <div class="workshop-item">
            <span class="dot dot-sage"></span>
            <div><div class="w-name">&#128187; Digital Inclusion</div><div class="w-org">Digital NNS</div><div class="w-url">digitalnns.org.uk</div></div>
        </div>
        <div class="workshop-item">
            <span class="dot dot-amber"></span>
            <div><div class="w-name">&#128274; Online Safety</div><div class="w-org">Digital NNS</div><div class="w-url">digitalnns.org.uk/first-fact-or-fiction-session</div></div>
        </div>
        <div class="workshop-item">
            <span class="dot dot-lavender"></span>
            <div><div class="w-name">&#128241; Everyday Tech</div><div class="w-org">Birmingham Settlement</div><div class="w-url">birminghamsettlement.org.uk/ladywood</div></div>
        </div>
        <div class="workshop-item">
            <span class="dot dot-mint"></span>
            <div><div class="w-name">&#129309; Community Connect</div><div class="w-org">Birmingham Settlement</div><div class="w-url">birminghamsettlement.org.uk/neighbourhood-futures-festival</div></div>
        </div>
    </div>

    <div class="reg-strip">
        <div>
            <div class="reg-strip-left">Register here &mdash; no account needed</div>
            <div class="reg-strip-sub">Fill in your details below or speak to a member of staff</div>
        </div>
        <div class="reg-fields">
            <div><div class="reg-field-label">FIRST NAME</div><div class="reg-field-line"></div></div>
            <div><div class="reg-field-label">LAST NAME</div><div class="reg-field-line"></div></div>
            <div><div class="reg-field-label">PHONE NUMBER</div><div class="reg-field-line"></div></div>
            <div><div class="reg-field-label">EMAIL (OPTIONAL)</div><div class="reg-field-line"></div></div>
        </div>
    </div>

    <div class="privacy">
        <strong>&#128274; Your Privacy (GDPR)</strong> &mdash;
        We only collect what you write here. Your name and phone confirm your place. Email (if given) is only used for reminders.
        Your details are never shared with third parties or used for marketing.
        Ask any staff member to delete your information at any time.
    </div>

    <div class="flyer-footer">Digital Inclusion Community Support System &nbsp;|&nbsp; Ladywood, Birmingham &nbsp;|&nbsp; Free &amp; Open to All</div>
</div>

</body>
</html>
"""

components.html(print_html, height=820, scrolling=True)