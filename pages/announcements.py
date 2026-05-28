### IMPORTS
import streamlit as st
import base64

### PAGE CONFIG
st.set_page_config(
    page_title="Announcements",
    layout="wide"
)

### FUNCTION FOR PNG ICON
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

announcement_icon = get_base64_image(
    "assets/megaphone.png"
)

### CUSTOM CSS
st.markdown("""
<style>
/* ---app background & streamlit overrides--- */
[data-testid="stAppViewContainer"]{
    background-color:#F5F2EA;
}

[data-testid="stHeader"]{
    background:transparent;
}

[data-testid="stToolbar"]{
    right:2rem;
}

[data-testid="stSidebar"]{
    display:none;
}

.block-container{
    max-width:none;
    width:100%;
    padding-top:2rem;
    padding-bottom:2rem;
    padding-left:4rem;
    padding-right:4rem;
}

/* ---back button styling--- */
.stButton > button{
    background:white;
    border-radius:18px;
    border:2px solid #D8D2C7;
    padding:12px 18px;
    font-size:18px;
    color:#444;
    margin-bottom:25px;
}

/* ---header--- */
.page-header{
    display:flex;
    align-items:center;
    gap:20px;
    margin-bottom:10px;
}

.page-header img{
    width:80px;
}
            
.page-title {
    font-size: 58px;
    font-weight: 900;
    color: #0D1B3D;
    margin-bottom: 5px;
}

.page-subtitle {
    font-size: 20px;
    color: #555;
    margin-bottom: 30px;
}
            
/* ---announcements box--- */
.subtitle-box{
    background:#CFEAC2;
    border:2px solid #A8D8A0;
    border-radius:24px;
    padding:20px 28px;
    margin-bottom:30px;
    font-size:18px;
    color:#1A3E1A;
}
            
/* ---announcements cards--- */
.announcement-card{
    background:white;
    border-radius:28px;
    padding:22px;
    margin-bottom:22px;
    display:flex;
    flex-direction:row;
    align-items:center;
    gap:24px;
    border:2px solid rgba(0,0,0,0.05);
    box-shadow:
    0 4px 12px rgba(0,0,0,0.04);
    transition:0.2s;
}

.announcement-card:hover{
    transform:scale(1.01);
}

.icon-box{
    width:110px;
    height:110px;
    border-radius:25px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:45px;
    flex-shrink:0;
}

/* card colours */
.green{
    background:#D8EBCF;
}

.purple{
    background:#E5D8F2;
}

.orange{
    background:#F7DFC8;
}

.pink{
    background:#F7D7DD;
}

.card-content{
    display:flex;
    flex-direction:column;
    justify-content:center;
    width:100%;
    margin:0;
    padding:0;
}
            
.card-content *{
    margin-left:0;
}

.card-content h3{
    margin:0;
    font-size:28px;
    color:#111;
}

.card-content p{
    margin-top:8px;
    font-size:18px;
    line-height:1.6;
    color:#555;
}

.view-button{
    background:#E3F2DB;
    border:2px solid #9ED492;
    border-radius:20px;
    padding:18px 30px;
    margin:35px auto 10px auto;
    width:320px;
    height:68px;
    display:flex;
    align-items:center;
    justify-content:center;
    position:relative;
    font-size:20px;
    font-weight:700;
    color:#3D6B32;
    transition:0.2s;
    box-shadow:0 4px 10px rgba(0,0,0,0.04);
}

.view-button span{
    position:absolute;
    right:28px;

    top:50%;
    transform:translateY(-50%);

    font-size:24px;
    line-height:1;
}

.view-button:hover{
    transform:translateY(-2px);
    background:#D6EDCB;
    box-shadow:0 8px 18px rgba(0,0,0,0.08);
}

.view-button:hover{
    transform:translateY(-2px);
    box-shadow:0 8px 18px rgba(0,0,0,0.08);
    background:#F8FFF5;
}

/* links */
a{
    text-decoration:none !important;
    color:inherit !important;
}

</style>
""", unsafe_allow_html=True)

### BACK BUTTON
if st.button("← Back to dashboard"):
    st.switch_page("app.py")

### HEADER
st.markdown("""
<div style="
    font-size:58px;
    font-weight:900;
    color:#0D1B3D;
    margin-bottom:10px;
">
📢 Announcements
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='subtitle-box'>
    Stay up to date with community news, local events,
    transport updates and important information for Ladywood residents.
</div>
""", unsafe_allow_html=True)

### ANNOUNCEMENTS
announcement_data = [
("🌳", "green", "Community Clean-Up Event", "Join the neighbourhood clean-up this Saturday at Ladywood Park. Everyone is welcome."),
("🚌", "purple", "Bus Route Changes", "Route 11 will have updated timings from next week. Check the Bus page for details."),
("🚧", "orange", "Roadworks on Richmond Road", "Temporary roadworks will take place from 25 May until 5 June."),
("❤️", "pink", "Free Health Check Event", "Free health checks available at the Neighbourhood Hub on 30 May.")
]

for icon, colour, card_title, text in announcement_data:

    st.markdown(
        f"""
<div class="announcement-card">

<div class="icon-box {colour}">
{icon}
</div>

<div class="card-content">

<h3>{card_title}</h3>

<p>{text}</p>

</div>

</div>
""",
        unsafe_allow_html=True
    )

### VIEW ALL BUTTON
st.markdown("""
<a href="https://www.birmingham.gov.uk/" target="_blank">

<div class="view-button">

<div>View All Announcements</div>

<span>→</span>

</div>

</a>
""", unsafe_allow_html=True)