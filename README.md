# Rainfall-Forecasting-Alert-System
real-time rainfall monitoring system that integrates external weather APIs, implements threshold-based alerting logic, and displays results through a web dashboard.
The system classifies rainfall into alert levels based on rainfall intensity thresholds and provides a user-friendly visualization inspired by modern weather applications.
To clone the repository use:
git clone https://github.com/your-username/rainfall-monitor.git
cd rainfall-monitor
To install the required libraries:
pip install -r requirements.txt
API Setup:
This project uses the OpenWeatherMap API.
After getting your API key, open weather_monitor.py and replace:
API_KEY = "YOUR_API_KEY"
with:
API_KEY = "your_actual_api_key"
Run the Streamlit dashboard:
python -m streamlit run weather_monitor.py
The dashboard includes:
Real-time rainfall display
Alert level visualization
Rainfall trend graph
City-based monitoring
Modern weather-style UI
