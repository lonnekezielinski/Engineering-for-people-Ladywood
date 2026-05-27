# NOTE: this is now only for the homepage not yet to navigate between pages. 

# To run: open terminal -> activate virtual environment: venv/Scripts/activate (Windows) or source venv/bin/activate (Mac) -> streamlit run app.py in terminal

# IMPORTS 
import streamlit as st
from PIL import Image

# PAGE CONFIG
st.set_page_config(
    page_title="Ladywood Connect",
    layout="wide"
)

# Custom css
st.markdown("""
<style>

.main {
    background-color: #F5F2EA;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}
            
.stButton > button {
    width: 100%;
    height: 220px;
    border-radius: 30px;
    font-size: 32px;
    font-weight: 600;
    border: 2px solid rgba(0,0,0,0.1);
    background-color: #DDB8E8;
    color: black;
    margin-bottom: 25px;
}

.title {
    font-size: 72px;
    font-weight: 800;
    color: #0D1B3D;
}

.subtitle {
    font-size: 24px;
    color: #444;
    margin-bottom: 40px;
}

.card {
    border-radius: 30px;
    padding: 40px;
    text-align: center;
    height: 220px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    font-size: 32px;
    font-weight: 600;
    margin-bottom: 25px;
    border: 2px solid rgba(0,0,0,0.1);
}

.bus {
    background-color: #DDB8E8;
}

.workshops {
    background-color: #C8E2F5;
}

.announcements {
    background-color: #CFEAC2;
}

.feedback {
    background-color: #F4D2BD;
}

.bottom-bar {
    margin-top: 40px;
}

</style>
""", unsafe_allow_html=True)

# Header
col1, col2 = st.columns([4,1])

with col1:
    st.markdown(
        '<div class="title">Ladywood Connect</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Your community hub</div>',
        unsafe_allow_html=True
    )

with col2:
    st.markdown("### 📅 26 May 2026")
    st.markdown("### ☀️ 18°C")
# We now have to set the temp, we could try to make it so that it becomes automatic. However i do think that for the prototype this is fine.

### BUTTON GRID
col1, col2 = st.columns(2)

# !!! change the emojies to pngs
# !! import pngs into the repository
with col1:

    if st.button("🚌 Bus", use_container_width=True):
        st.switch_page("pages/bus.py")

    if st.button("📢 Announcements", use_container_width=True):
        st.switch_page("pages/announcements.py")

with col2:

    if st.button("📅 Workshops", use_container_width=True):
        st.switch_page("pages/workshops.py")

    if st.button("💬 Feedback & Requests", use_container_width=True):
        st.switch_page("pages/feedback.py")

# BOTTOM SETTINGS
bottom1, bottom2 = st.columns([1,1])

with bottom1:
    language = st.selectbox(
        "Language",
        ["English", "Arabic", "Urdu", "Punjabi"]
    )

with bottom2:
    text_size = st.radio(
        "Text size",
        ["A", "A+", "A++"],
        horizontal=True
    )