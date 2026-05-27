import streamlit as st

st.title("Bus Information")

st.write("Live transport updates and schedules.")

import streamlit as st
import folium
from streamlit_folium import st_folium

# PAGE CONFIG
st.set_page_config(page_title="Bus - Ladywood Connect", layout="wide")

### CUSTOM CSS
st.markdown("""
<style>
[data-testid="stAppViewContainer"] { background-color: #F5F2EA; }
[data-testid="stHeader"] { background-color: transparent; }
[data-testid="stSidebar"] { display: none; }
.block-container { padding-top: 2rem; padding-bottom: 2rem; }

.page-title {
    font-size: 58px;
    font-weight: 900;
    color: #0D1B3D;
    margin-bottom: 5px;
}
.section-title {
    font-size: 28px;
    font-weight: 700;
    color: #0D1B3D;
    margin-top: 30px;
    margin-bottom: 10px;
}
.info-box {
    background: #DDB8E8;
    border: 2px solid #c99de0;
    border-radius: 24px;
    padding: 20px 28px;
    margin-bottom: 20px;
    font-size: 18px;
    color: #2a1a3e;
}
.live-badge {
    display: inline-block;
    background: #CFEAC2;
    color: #2a6e1f;
    font-weight: 700;
    font-size: 16px;
    border-radius: 20px;
    padding: 6px 18px;
    margin-bottom: 16px;
    border: 2px solid #a8d8a0;
}
.schedule-box {
    background: #C8E2F5;
    border: 2px solid #a0c8e8;
    border-radius: 24px;
    padding: 20px 28px;
    margin-bottom: 10px;
}
.tip-box {
    background: #F4D2BD;
    border: 2px solid #e0b89a;
    border-radius: 24px;
    padding: 20px 28px;
    margin-top: 20px;
    font-size: 18px;
    color: #5a2e0e;
}
.day-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px 0;
    border-bottom: 1px solid #b8d4e8;
    font-size: 17px;
    color: #0D1B3D;
}
.day-name { font-weight: 700; width: 120px; }
.day-time { color: #444; }
.closed { color: #cc4444; font-weight: 600; }
a { text-decoration: none !important; color: inherit !important; }
</style>
""", unsafe_allow_html=True)

# BACK BUTTON
st.markdown('<a href="/" target="_self">← Back to Home</a>', unsafe_allow_html=True)

# TITLE
st.markdown('<div class="page-title">🚌 Community Bus</div>', unsafe_allow_html=True)

st.markdown("""
<div class='info-box'>
    🌟 Our community bus brings <strong>free internet</strong> right to your 
    neighbourhood in Ladywood! Come visit us — everyone is welcome 💜
</div>
""", unsafe_allow_html=True)

# LIVE LOCATION
st.markdown('<div class="section-title">📍 Where is the bus this week?</div>', unsafe_allow_html=True)
st.markdown('<div class="live-badge">🟢 Parked here all week!</div>', unsafe_allow_html=True)

# Ladywood Leisure Centre, Birmingham - real coordinates
bus_lat = 52.47927
bus_lon = -1.91598

# Real Ladywood map using OpenStreetMap
m = folium.Map(
    location=[bus_lat, bus_lon],
    zoom_start=16,
    tiles="OpenStreetMap"
)

# Colourful circle around bus location
folium.CircleMarker(
    location=[bus_lat, bus_lon],
    radius=30,
    color="#DDB8E8",
    fill=True,
    fill_color="#DDB8E8",
    fill_opacity=0.5,
).add_to(m)

# Bus marker
folium.Marker(
    location=[bus_lat, bus_lon],
    popup=folium.Popup("""
        <div style='font-family:sans-serif; text-align:center; padding:5px;'>
            <h3 style='color:#6a0dad; margin:0;'>🚌 Community Bus</h3>
            <p style='margin:5px 0;'>📍 Ladywood Leisure Centre</p>
            <p style='margin:5px 0;'>⏰ Mon–Fri: 9:00–16:00</p>
            <p style='margin:5px 0; color:#cc4444;'>❌ Closed weekends</p>
        </div>
    """, max_width=220),
    tooltip="🚌 Community Bus — click for info!",
    icon=folium.Icon(color="purple", icon="bus", prefix="fa")
).add_to(m)

st_folium(m, width="100%", height=420)

st.markdown("""
<div class='info-box' style='background:#CFEAC2; border-color:#a8d8a0; color:#1a3e1a;'>
    📌 <strong>Ladywood Leisure Centre</strong>, Ladywood Middleway, Birmingham B16 8DN<br>
    🚶 5 minute walk from Five Ways Station
</div>
""", unsafe_allow_html=True)

# WEEKLY SCHEDULE
st.markdown('<div class="section-title">🗓️ Opening Hours This Week</div>', unsafe_allow_html=True)

st.markdown("""
<div class='schedule-box'>
    <div class='day-row'>
        <span class='day-name'>Monday</span>
        <span class='day-time'>⏰ 9:00 – 16:00</span>
    </div>
    <div class='day-row'>
        <span class='day-name'>Tuesday</span>
        <span class='day-time'>⏰ 9:00 – 16:00</span>
    </div>
    <div class='day-row'>
        <span class='day-name'>Wednesday</span>
        <span class='day-time'>⏰ 9:00 – 16:00</span>
    </div>
    <div class='day-row'>
        <span class='day-name'>Thursday</span>
        <span class='day-time'>⏰ 9:00 – 16:00</span>
    </div>
    <div class='day-row'>
        <span class='day-name'>Friday</span>
        <span class='day-time'>⏰ 9:00 – 16:00</span>
    </div>
    <div class='day-row'>
        <span class='day-name'>Saturday</span>
        <span class='day-time closed'>❌ Closed</span>
    </div>
    <div class='day-row' style='border-bottom:none;'>
        <span class='day-name'>Sunday</span>
        <span class='day-time closed'>❌ Closed</span>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='tip-box'>
    💡 <strong>Good to know!</strong> The bus internet is completely free — 
    just show up and connect! No registration or ID needed. 🎉
</div>
""", unsafe_allow_html=True)