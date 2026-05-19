"""
Rainfall Monitoring Dashboard - Modern Weather App Style
"""

import streamlit as st
import requests
from datetime import datetime
import pandas as pd
import numpy as np

# =============================================================================
# Configuration
# =============================================================================

API_KEY = "bd5e378503939ddaee76f12ad7a97608"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

st.set_page_config(
    page_title="Stormy - Rainfall Monitor",
    page_icon="🌧️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =============================================================================
# Custom CSS
# =============================================================================

def load_custom_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

    /* Main App Background */
    .stApp {
        font-family: 'Poppins', sans-serif;
        background: linear-gradient(180deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        background-attachment: fixed;
    }

    /* Header Styling */
    .main-title {
        font-size: 3.5rem;
        font-weight: 700;
        color: white !important;
        text-align: center;
        margin-bottom: 0.5rem;
    }

    .subtitle {
        text-align: center;
        color: #a0a0b0;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }

    /* Weather Card with Glass Effect */
    .weather-card {
        background: rgba(255,255,255,0.08);
        backdrop-filter: blur(12px);
        border-radius: 24px;
        padding: 2.5rem;
        border: 1px solid rgba(255,255,255,0.1);
        box-shadow: 0 8px 32px rgba(0,0,0,0.3);
    }

    /* Large Rainfall Display */
    .rainfall-value {
        font-size: 7rem;
        font-weight: 700;
        color: #ffffff;
        line-height: 1.1;
    }

    .rainfall-unit {
        font-size: 1.5rem;
        color: #a0a0b0;
        margin-left: 0.25rem;
    }

    .weather-desc {
        font-size: 1.4rem;
        color: #ffffff;
        margin-top: 0.75rem;
    }

    /* Alert Badge with Spacing Fix */
    .alert-badge {
        display: inline-block;
        padding: 0.6rem 2rem;
        border-radius: 50px;
        font-weight: 700;
        font-size: 1.2rem;
        letter-spacing: 1px;
        margin-top: 1rem;
    }

    .alert-green {
        background: linear-gradient(135deg, #00b09b, #96c93d);
        color: white;
    }

    .alert-yellow {
        background: linear-gradient(135deg, #f7971e, #ffd200);
        color: #1a1a2e;
    }

    .alert-red {
        background: linear-gradient(135deg, #cb2d3e, #ef473a);
        color: white;
    }

    /* Right Column - Alert Section Spacing */
    .alert-section {
        display: flex;
        flex-direction: column;
        align-items: flex-end;
        justify-content: flex-start;
        padding-top: 0.5rem;
        height: 100%;
    }

    .city-info {
        margin-top: 2rem;
        text-align: right;
    }

    .info-text {
        color: #a0a0b0;
        font-size: 0.95rem;
    }

    /* Input Field Styling */
    .stTextInput input {
        color: black !important;
        background: rgba(255,255,255,0.08) !important;
        border: 1px solid rgba(255,255,255,0.15) !important;
        border-radius: 12px;
        padding: 0.75rem 1rem;
        font-size: 1rem;
    }

    .stTextInput input::placeholder {
        color: rgba(255,255,255,0.4);
    }

    /* Button Styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.75rem 1.5rem;
        font-weight: 600;
        font-size: 1rem;
    }

    /* Chart Section */
    .chart-container {
        background: rgba(255,255,255,0.05);
        border-radius: 16px;
        padding: 1.5rem;
        margin: 1rem 0;
    }

    /* Section Titles - White */
    .section-title {
        color: #ffffff !important;
        font-weight: 600;
        margin-bottom: 1rem;
    }


    .alert-guide-item {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        margin: 0.75rem 0;
        color: #a0a0b0;
    }

    .alert-guide-item strong {
        color: #ffffff;
    }

    /* Spacing between sections */
    .section-spacer {
        margin: 1.5rem 0;
    }

    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)


# =============================================================================
# Core Functions
# =============================================================================

@st.cache_data(ttl=300)
def fetch_weather(city: str):
    params = {"q": city, "appid": API_KEY, "units": "metric"}

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()

        rainfall = data.get("rain", {}).get("1h", 0.0)

        return {
            "rainfall": rainfall,
            "city": data.get("name", city),
            "country": data.get("sys", {}).get("country", ""),
            "success": True
        }

    except:
        return {"success": False}


def check_alert(rainfall):
    if rainfall < 10:
        return "GREEN", "✅ Normal Conditions"
    elif rainfall < 20:
        return "YELLOW", "⚠️ Moderate Rainfall"
    else:
        return "RED", "🚨 Heavy Rainfall Alert"


def generate_dummy_data():
    hours = [f"{i:02d}:00" for i in range(1, 25)]
    values = np.clip(np.random.exponential(2, 24), 0, 30)
    return pd.DataFrame({"Hour": hours, "Rain": values})


# =============================================================================
# Main App
# =============================================================================

def main():
    load_custom_css()

    # Header
    st.markdown('<h1 class="main-title">🌧️ Stormy</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Real-time Rainfall Monitoring</p>', unsafe_allow_html=True)

    st.markdown(f"<p style='text-align:center;'>🕐 {datetime.now().strftime('%H:%M')}</p>", unsafe_allow_html=True)

    # Input Section with proper spacing
    st.markdown('<div class="section-spacer"></div>', unsafe_allow_html=True)

    col1, col2 = st.columns([3, 1])

    with col1:
        city = st.text_input("🌍 Enter city name", placeholder="e.g., London, Tokyo, Paris", label_visibility="collapsed", key="city_input")

    with col2:
        check = st.button("🔍 Check Weather", use_container_width=True)

    # Main
    if check and city:
        data = fetch_weather(city)

        if data["success"]:
            rain = data["rainfall"]
            level, desc = check_alert(rain)

            st.markdown('<div class="weather-card">', unsafe_allow_html=True)

            col_left, col_right = st.columns([2, 1])

            with col_left:
                st.markdown(f"""
                <span class="rainfall-value">{rain:.1f}</span>
                <span class="rainfall-unit"> mm/h</span>
                <p class="weather-desc">{desc}</p>
                """, unsafe_allow_html=True)

            with col_right:
                level_lower = level.lower()
                st.markdown(f"""
                <div class="alert-section">
                    <span class="alert-badge alert-{level_lower}">{level}</span>
                    <div class="city-info">
                        <p class="info-text">📍 {data['city']}, {data['country']}</p>
                        <p class="info-text">🕐 Updated: {datetime.now().strftime('%H:%M')}</p>
                    </div>
                </div>
                """, unsafe_allow_html=True)

            st.markdown('</div>', unsafe_allow_html=True)

            # Chart + Alert Guide - Improved Layout
            st.markdown('<div class="section-spacer"></div>', unsafe_allow_html=True)

            col_chart, col_info = st.columns([3, 1])

            # Chart Section (Left - Larger)
            with col_chart:
                st.markdown('<p class="section-title">📈 Recent Rainfall Trend (Last 24 Hours)</p>', unsafe_allow_html=True)

                chart_data = generate_dummy_data()
                chart_data = chart_data.set_index("Hour")

                st.line_chart(
                    chart_data["Rain"],
                    height=420,
                    width='stretch',
                )

            # Alert Guide (Right - Pushed to edge)
            with col_info:
                st.markdown("""
                <div class="alert-guide">
                    <p class="section-title" style="font-size:1.1rem;">📋 Alert Guide</p>
                    <div class="alert-guide-item">
                        <span>🟢</span> <strong>GREEN</strong> → &lt;10 mm/h <br><span style="color:#888;font-size:0.85rem;">Normal</span>
                    </div>
                    <div class="alert-guide-item">
                        <span>🟡</span> <strong>YELLOW</strong> → 10-20 mm/h <br><span style="color:#888;font-size:0.85rem;">Moderate</span>
                    </div>
                    <div class="alert-guide-item">
                        <span>🔴</span> <strong>RED</strong> → ≥20 mm/h <br><span style="color:#888;font-size:0.85rem;">Alert</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)

        else:
            st.error("❌ Error fetching data")

    else:
        st.markdown("""
        <div class="weather-card" style="text-align:center; padding:3rem;">
            <h2 style="color:#ffffff; margin-bottom:1rem;">👋 Welcome to Stormy</h2>
            <p class="info-text" style="font-size:1.1rem;">Enter a city name above to check current rainfall conditions</p>
            <p style="font-size:4rem; margin:1.5rem 0;">🌧️</p>
        </div>
        """, unsafe_allow_html=True)


# Run
if __name__ == "__main__":
    main()
