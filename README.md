# 🌧️ Rainfall-Forecasting-Alert-System

real-time rainfall monitoring system that integrates external weather APIs, implements threshold-based alerting logic, and displays results through a web dashboard.
The system classifies rainfall into alert levels based on rainfall intensity thresholds and provides a user-friendly visualization inspired by modern weather applications.

---

## ✨ Features

- 🌍 Real-time rainfall monitoring by city
- 🚨 Threshold-based rainfall alerts
- 📊 Interactive rainfall trend visualization
- 🎨 Modern weather-app-inspired interface
- ⚡ Real-time API integration using OpenWeatherMap
- 🕒 Live timestamp updates
- 📱 Responsive Streamlit dashboard
- 🧠 AI-assisted development workflow

---

## 🚦 Alert Levels

| Alert Level | Rainfall Intensity | Status |
|---|---|---|
| 🟢 GREEN | < 10 mm/h | Normal Conditions |
| 🟡 YELLOW | 10 – 20 mm/h | Moderate Rainfall |
| 🔴 RED | ≥ 20 mm/h | Heavy Rainfall Alert |

---

## 🛠️ Technologies Used

- Python 3.10+
- Streamlit
- Requests
- Pandas
- NumPy
- OpenWeatherMap API

---

## 📂 Project Structure

```text
rainfall_monitor_project/
│
├── weather_monitor.py      # Main Streamlit application
├── alert_log.txt           # Logged rainfall alerts
├── prompt_log.md           # AI interaction documentation
├── requirements.txt        # Required Python libraries
└── README.md               # Project documentation
```
## Clone the Repository

git clone https://github.com/Qaiseu/rainfall-monitor.git
cd rainfall-monitor

## Install Required Libraries

pip install -r requirements.txt

## Running the Application

python -m streamlit run weather_monitor.py
