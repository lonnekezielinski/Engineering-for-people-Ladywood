import streamlit as st

st.set_page_config(
    page_title="Feedback & Requests",
    layout="wide"
)

st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background-color:#F5F2EA;
}

[data-testid="stHeader"] {
    background:transparent;
}

[data-testid="stSidebar"] {
    display:none;
}

.block-container {
    padding-top:2rem;
    padding-bottom:2rem;
    padding-left:3rem;
    padding-right:3rem;
}

/* back button */
.stButton > button {
    background:white;
    border-radius:18px;
    border:2px solid #D8D2C7;
    padding:12px 18px;
    font-size:18px;
    color:#444;
    margin-bottom:25px;
}

/* page title */
.page-title {
    font-size:58px;
    font-weight:900;
    color:#0D1B3D;
    margin-bottom:8px;
}

.page-subtitle {
    font-size:20px;
    color:#444;
    margin-bottom:25px;
}

/* --- HEADER --- */

.page-header{
    display:flex;
    align-items:center;
    gap:20px;
    margin-bottom:20px;
}

.header-icon{
    font-size:70px;
}

.page-title{
    font-size:64px;
    font-weight:900;
    color:#0D1B3D;
}

/* subtitle/info box */

.intro-box{
    background:#F4D2BD;

    border:2px solid #E4B999;

    border-radius:28px;

    padding:28px 34px;

    margin-bottom:35px;

    font-size:22px;

    line-height:1.6;

    color:#5A2E0E;
} 

/* info box */
.intro-box {
    background:#F4D2BD;
    border:2px solid #E4B999;
    border-radius:24px;
    padding:22px 28px;
    margin-bottom:30px;
    font-size:19px;
    color:#5A2E0E;
    line-height:1.5;
}

/* cards */
.panel {
    background:white;
    border:2px solid rgba(0,0,0,0.06);
    border-radius:28px;
    padding:28px;
    margin-bottom:25px;
    box-shadow:0 4px 12px rgba(0,0,0,0.04);
}

.panel-title {
    font-size:28px;
    font-weight:800;
    color:#0D1B3D;
    margin-bottom:20px;
}

.help-row {
    display:flex;
    gap:18px;
    align-items:flex-start;
    margin-bottom:24px;
}

.help-icon {
    width:64px;
    height:64px;
    border-radius:50%;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:30px;
    flex-shrink:0;
}

.blue { background:#D9ECFA; }
.green { background:#D8EBCF; }
.purple { background:#E5D8F2; }
.orange { background:#F7DFC8; }

.help-title {
    font-size:20px;
    font-weight:800;
    color:#0D1B3D;
}

.help-text {
    font-size:17px;
    color:#444;
}

/* request list */
.request-card {
    background:#FAFAFA;
    border:2px solid rgba(0,0,0,0.06);
    border-radius:20px;
    padding:18px;
    margin-bottom:14px;
    display:flex;
    align-items:center;
    gap:18px;
}

.request-icon {
    width:64px;
    height:64px;
    border-radius:16px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:32px;
    flex-shrink:0;
}

.request-title {
    font-size:19px;
    font-weight:800;
    color:#0D1B3D;
}

.request-meta {
    font-size:15px;
    color:#555;
    margin-top:4px;
}

.status {
    margin-left:auto;
    padding:8px 14px;
    border-radius:18px;
    font-size:14px;
    font-weight:700;
}

.in-progress {
    background:#D9ECFA;
    color:#1C6BB0;
}

.under-review {
    background:#F7DFC8;
    color:#A35E00;
}

.completed {
    background:#D8EBCF;
    color:#287A3E;
}

.closed {
    background:#E8E8E8;
    color:#555;
}

/* form styling */
div[data-baseweb="select"] > div,
textarea,
input {
    border-radius:16px !important;
}

.stTextArea textarea {
    min-height:170px;
}

/* submit button */
div[data-testid="stFormSubmitButton"] button {
    width:100%;
    background:#7B3FB2;
    color:white;
    border:none;
    border-radius:16px;
    padding:16px;
    font-size:20px;
    font-weight:700;
}

div[data-testid="stFormSubmitButton"] button:hover {
    background:#6A329E;
    color:white;
}
            
/* ---tabs--- */
.stTabs [data-baseweb="tab-list"] {
    gap: 14px;
    margin-bottom: 30px;
    border-bottom: 2px solid #D8D2C7;
}

.stTabs [data-baseweb="tab"] {
    background: #F5F2EA;
    border: 2px solid #D8D2C7;
    border-bottom: none;
    border-radius: 18px 18px 0 0;
    padding: 14px 32px;
    font-size: 30px;
    font-weight: 700;
    color: #555;
    height: 65px;
}

/* make emoji + text bigger */
.stTabs [data-baseweb="tab"] p {
    font-size: 18px;
}

.stTabs [aria-selected="true"] {
    background: white !important;
    color: #7B3FB2 !important;
    border-bottom: 5px solid #7B3FB2 !important;
}
            
/* Make form inputs light */
input,
textarea,
[data-baseweb="select"] > div {
    background-color:white !important;
    color:#0D1B3D !important;
    border:2px solid #D8D2C7 !important;
}

textarea::placeholder,
input::placeholder {
    color:#777 !important;
}
            
/* force form labels and input text to be readable */
[data-testid="stSelectbox"] label p,
[data-testid="stTextArea"] label p,
[data-testid="stTextInput"] label p {
    color:#0D1B3D !important;
    font-weight:700 !important;
    font-size:17px !important;
}

input,
textarea,
[data-baseweb="select"] > div {
    background:white !important;
    color:#0D1B3D !important;
    border:2px solid #D8D2C7 !important;
}

textarea::placeholder,
input::placeholder {
    color:#777 !important;
}
            
/* success message */
[data-testid="stAlert"] {
    background-color: #D8EBCF !important;
    border: 2px solid #9ED18F !important;
    border-radius: 18px !important;
}

[data-testid="stAlert"] p {
    color: #1E4D2B !important;
    font-size: 18px !important;
    font-weight: 700 !important;
}

</style>
""", unsafe_allow_html=True)

### BACK BUTTON
if st.button("← Back to dashboard"):
    st.switch_page("app.py")

### HEADER
st.markdown("""
<div style="font-size:58px;font-weight:900;color:#0D1B3D;margin-bottom:10px;">
💬 Feedback & Requests
</div>
""", unsafe_allow_html=True)

### INFO BOX
st.markdown("""
<div class="intro-box">
<strong>🧡 We value your voice.</strong><br>
Share your feedback or request a service. Together, we make Ladywood better.
Your feedback and requests help us improve services and create a stronger community.
</div>
""", unsafe_allow_html=True)

### TABS
feedback_tab, requests_tab = st.tabs(["💬 Feedback", "📝 Requests"])

### FEEDBACK TAB
with feedback_tab:

    left, right = st.columns([1.1, 1])

    with left:
        with st.container():
            st.markdown('<div class="panel-title">Send us your feedback</div>', unsafe_allow_html=True)

            with st.form("feedback_form"):
                feedback_topic = st.selectbox(
                    "What is your feedback about?",
                    ["Select a topic", "Community bus", "Workshops", "Announcements", "Accessibility", "Other"]
                )

                feedback_text = st.text_area(
                    "Tell us more",
                    placeholder="Write your feedback, suggestion or request here..."
                )

                feedback_name = st.text_input(
                    "Your name (optional)",
                    placeholder="Enter your name"
                )

                submitted = st.form_submit_button("➤ Send Feedback")

                if submitted:
                    st.success("Thank you! Your feedback has been submitted.")

    with right:
        st.markdown("""
<div class="panel">
<div class="panel-title">What happens next?</div>
<div class="help-row"><div class="help-icon blue">🔍</div><div><div class="help-title">We review</div><div class="help-text">Our team reads all feedback carefully.</div></div></div>
<div class="help-row"><div class="help-icon green">✅</div><div><div class="help-title">We take action</div><div class="help-text">We use your input to improve our services.</div></div></div>
<div class="help-row"><div class="help-icon purple">📢</div><div><div class="help-title">We keep you updated</div><div class="help-text">We share updates when changes are made.</div></div></div>
</div>
""", unsafe_allow_html=True)
    
        st.markdown("""
<div class="panel">
<div class="panel-title">Other ways to get in touch</div>

<div class="request-card">
<div class="request-icon orange">📞</div>
<div>
<div class="request-title">Call us</div>
<div class="request-meta">0121 345 6789</div>
</div>
</div>

<div class="request-card">
<div class="request-icon orange">✉️</div>
<div>
<div class="request-title">Email us</div>
<div class="request-meta">info@ladywoodconnect.org</div>
</div>
</div>

</div>
""", unsafe_allow_html=True)

### REQUESTS TAB
with requests_tab:

    left, right = st.columns([1.1, 1])

    with left:

        st.markdown(
            '<div class="panel-title">Send us a request</div>',
            unsafe_allow_html=True
        )

        with st.form("request_form"):
            request_topic = st.selectbox(
                "What is your request about?",
                [
                    "Select a topic",
                    "Transport",
                    "Parks & Environment",
                    "Community activities",
                    "Waste & Cleanliness",
                    "Safety",
                    "Other"
                ]
            )

            request_text = st.text_area(
                "Tell us more",
                placeholder="Describe your request in as much detail as possible..."
            )

            request_name = st.text_input(
                "Your name (optional)",
                placeholder="Enter your name"
            )

            request_submitted = st.form_submit_button("➤ Send Request")

            if request_submitted:
                st.success("Thank you! Your request has been submitted.")

    with right:

        st.markdown("""
<div class="panel">
<div class="panel-title">Your requests</div>
<div style="font-size:17px;color:#555;margin-bottom:20px;">
View, track and manage the requests you've made.
</div>

<div class="request-card">
<div class="request-icon orange">🚌</div>
<div>
<div class="request-title">Request for better bus shelter</div>
<div class="request-meta">Transport · Submitted 5 days ago</div>
</div>
<div class="status in-progress">In progress</div>
</div>

<div class="request-card">
<div class="request-icon green">🌳</div>
<div>
<div class="request-title">Fix lighting in the park</div>
<div class="request-meta">Parks & Environment · Submitted 1 week ago</div>
</div>
<div class="status under-review">Under review</div>
</div>

<div class="request-card">
<div class="request-icon purple">👥</div>
<div>
<div class="request-title">Request for youth activities</div>
<div class="request-meta">Community · Submitted 2 weeks ago</div>
</div>
<div class="status completed">Completed</div>
</div>

<div class="request-card">
<div class="request-icon orange">🗑️</div>
<div>
<div class="request-title">More frequent bin collection</div>
<div class="request-meta">Waste & Cleanliness · Submitted 2 weeks ago</div>
</div>
<div class="status closed">Closed</div>
</div>

<div style="text-align:center;margin-top:20px;font-weight:700;color:#7B3FB2;">
View all requests ›
</div>
</div>
""", unsafe_allow_html=True)