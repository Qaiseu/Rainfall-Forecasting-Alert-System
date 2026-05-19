# Prompt Log - Specialized Experiment 1
# Short-term Rainfall Forecasting & Alert System

# Prompt1 API Integration:
I am a water resources engineering student building a rainfall monitoring system.

Please write a Python function called fetch_weather(city) that uses the OpenWeatherMap API to retrieve current weather data.

Requirements:
1. Use the requests library
2. Send a GET request to: https://api.openweathermap.org/data/2.5/weather
3. Accept city name as input
4. Extract rainfall intensity in mm/h from the JSON response
   - If "rain" field does not exist, return 0
5. Handle API errors (invalid key, connection issues, etc.)
6. Return rainfall value as a float
7. Add clear comments explaining each step

Use a placeholder API key: "YOUR_API_KEY"

# AI generated answer: 
```python
import requests


def fetch_weather(city: str) -> float:
    """
    Fetches current weather data for a given city from OpenWeatherMap API
    and extracts rainfall intensity in mm/h.

    Args:
        city: Name of the city to fetch weather data for.

    Returns:
        Rainfall intensity in mm/h (float). Returns 0 if no rain data available.
    """
    # OpenWeatherMap API configuration
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    api_key = "YOUR_API_KEY"

    # Prepare request parameters
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Get temperature in Celsius, rainfall in mm
    }

    try:
        # Send GET request to OpenWeatherMap API
        response = requests.get(base_url, params=params, timeout=10)

        # Raise an exception for HTTP errors (4xx, 5xx status codes)
        response.raise_for_status()

        # Parse JSON response
        data = response.json()

        # Extract rainfall intensity from the response
        # OpenWeatherMap returns rainfall data under the "rain" key
        # The "1h" field contains rainfall in the last 1 hour (mm)
        if "rain" in data and "1h" in data["rain"]:
            rainfall_intensity = float(data["rain"]["1h"])
        else:
            # No rain data available - return 0
            rainfall_intensity = 0.0

        return rainfall_intensity

    except requests.exceptions.HTTPError as e:
        # Handle HTTP errors (e.g., 401 Unauthorized - invalid API key, 404 Not Found)
        print(f"HTTP Error: {e}")
        raise

    except requests.exceptions.ConnectionError as e:
        # Handle connection issues (network problems, DNS failures)
        print(f"Connection Error: {e}")
        raise

    except requests.exceptions.Timeout as e:
        # Handle request timeout
        print(f"Timeout Error: {e}")
        raise

    except requests.exceptions.RequestException as e:
        # Catch any other request-related errors
        print(f"Request Error: {e}")
        raise

    except (ValueError, KeyError) as e:
        # Handle JSON parsing errors or missing expected fields
        print(f"Data Error: {e}")
        raise


if __name__ == "__main__":
    # Example usage
    city_name = "London"
    rainfall = fetch_weather(city_name)
    print(f"Rainfall intensity in {city_name}: {rainfall} mm/h")
```

**Usage:**
```bash
pip install requests
```

Then replace `"YOUR_API_KEY"` with your actual OpenWeatherMap API key (free at openweathermap.org). The function returns rainfall in mm/h, or `0.0` if no rain is detected.

# Comment: 
this is actually a very good output from OpenCode it's clean, correct, and matches the requirements, I only had to replace the API key with the one i got from  OpenWeatherMap

# Prompt2 Alert Logic:
I am building a rainfall monitoring system.

Please write a Python function called check_alert(rainfall) that:

1. Takes rainfall (float) as input
2. Returns alert level based on:
   - "GREEN" if rainfall < 10
   - "YELLOW" if 10 <= rainfall < 20
   - "RED" if rainfall >= 20
3. Also return a message:
   - GREEN → "Normal conditions"
   - YELLOW → "Moderate rainfall"
   - RED → "Heavy rainfall - ALERT"
4. Add comments explaining the logic

# AI generated result:
```python
def check_alert(rainfall: float) -> tuple[str, str]:
    """
    Determines the alert level and message based on rainfall intensity.

    Args:
        rainfall: Rainfall intensity in mm/h.

    Returns:
        A tuple containing (alert_level, message).
        - alert_level: "GREEN", "YELLOW", or "RED"
        - message: Human-readable description of conditions
    """
    # Check rainfall intensity against thresholds
    # Thresholds are based on typical water resources engineering standards
    # where 10 mm/h marks moderate rain and 20 mm/h indicates heavy rain
    
    if rainfall < 10:
        # Low rainfall - normal conditions, no action needed
        alert_level = "GREEN"
        message = "Normal conditions"
    
    elif rainfall < 20:
        # Moderate rainfall - conditions warrant monitoring
        alert_level = "YELLOW"
        message = "Moderate rainfall"
    
    else:
        # Heavy rainfall - potential flooding risk, immediate alert
        alert_level = "RED"
        message = "Heavy rainfall - ALERT"
    
    return alert_level, message


if __name__ == "__main__":
    # Example usage
    test_rainfall = [0.0, 5.0, 10.0, 15.0, 20.0, 25.0]
    
    for rain in test_rainfall:
        level, msg = check_alert(rain)
        print(f"Rainfall: {rain} mm/h → {level}: {msg}")
```

**Output:**
```
Rainfall: 0.0 mm/h → GREEN: Normal conditions
Rainfall: 5.0 mm/h → GREEN: Normal conditions
Rainfall: 10.0 mm/h → YELLOW: Moderate rainfall
Rainfall: 15.0 mm/h → YELLOW: Moderate rainfall
Rainfall: 20.0 mm/h → RED: Heavy rainfall - ALERT
Rainfall: 25.0 mm/h → RED: Heavy rainfall - ALERT
```

# Comment: 
This part is already 100% correct and clean also,but right now we have two separate programs:
fetch_weather() → gets rainfall
check_alert() → analyzes rainfall
They are NOT connected yet, I did combine them together but then i thought maybe it will be easier to just make the AI do it but for now the code works perfectly and gives the following output: City: London
Rainfall: 0.0 mm/h
Alert Level: GREEN
Message: Normal conditions

# prompt3 Integration:
I am building a rainfall monitoring system in Python.

I already have two functions:
1. fetch_weather(city) → returns rainfall intensity (mm/h) using OpenWeather API
2. check_alert(rainfall) → returns (alert_level, message) based on thresholds

Please combine them into a single complete Python program.

Requirements:
1. Keep both functions (fetch_weather and check_alert)
2. In the main section:
   - Ask for a city name (or define one)
   - Call fetch_weather(city) to get rainfall
   - Pass rainfall to check_alert(rainfall)
3. Print a clear output:
   - City name
   - Rainfall (mm/h)
   - Alert level
   - Message
4. Handle errors gracefully (if API fails, rainfall should be 0.0)
5. Add comments explaining the flow of the program
6. Keep the code clean and well-structured

Optional:
- Add a small test with multiple cities

# AI generated result: 
```python
"""
Rainfall Monitoring System
Retrieves weather data and provides flood alert levels for water resources monitoring.
"""

import requests


def fetch_weather(city: str) -> float:
    """
    Fetches current weather data for a given city from OpenWeatherMap API.

    Args:
        city: Name of the city to fetch weather data for.

    Returns:
        Rainfall intensity in mm/h. Returns 0.0 if no rain data or error occurs.
    """
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    api_key = "YOUR_API_KEY"

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        if "rain" in data and "1h" in data["rain"]:
            return float(data["rain"]["1h"])
        return 0.0

    except requests.exceptions.RequestException as e:
        # Log error but return 0 to allow graceful degradation
        print(f"Warning: Could not fetch weather for {city}: {e}")
        return 0.0


def check_alert(rainfall: float) -> tuple[str, str]:
    """
    Determines alert level based on rainfall intensity.

    Args:
        rainfall: Rainfall intensity in mm/h.

    Returns:
        Tuple of (alert_level, message).
    """
    if rainfall < 10:
        alert_level = "GREEN"
        message = "Normal conditions"
    elif rainfall < 20:
        alert_level = "YELLOW"
        message = "Moderate rainfall"
    else:
        alert_level = "RED"
        message = "Heavy rainfall - ALERT"

    return alert_level, message


def monitor_city(city: str) -> dict:
    """
    Monitors rainfall and alert status for a single city.
    Combines fetching weather data with alert checking.

    Args:
        city: Name of the city to monitor.

    Returns:
        Dictionary containing city, rainfall, alert_level, and message.
    """
    rainfall = fetch_weather(city)
    alert_level, message = check_alert(rainfall)

    return {
        "city": city,
        "rainfall_mm_h": rainfall,
        "alert_level": alert_level,
        "message": message
    }


def print_report(report: dict) -> None:
    """
    Prints a formatted monitoring report.

    Args:
        report: Dictionary containing monitoring results.
    """
    print("=" * 50)
    print(f"  RAINFALL MONITORING REPORT")
    print("=" * 50)
    print(f"  City:           {report['city']}")
    print(f"  Rainfall:       {report['rainfall_mm_h']} mm/h")
    print(f"  Alert Level:    {report['alert_level']}")
    print(f"  Status:         {report['message']}")
    print("=" * 50)


def main():
    """
    Main entry point for the rainfall monitoring system.
    """
    # Option 1: Monitor a single city (uncomment to use)
    # city = input("Enter city name: ")
    # report = monitor_city(city)
    # print_report(report)

    # Option 2: Run test with multiple cities
    test_cities = ["London", "Tokyo", "Miami", "Sydney"]

    print("\nRunning rainfall monitoring for multiple cities...\n")

    for city in test_cities:
        report = monitor_city(city)
        print_report(report)
        print()


if __name__ == "__main__":
    main()
```

**Sample Output:**
```
Running rainfall monitoring for multiple cities...

==================================================
  RAINFALL MONITORING REPORT
==================================================
  City:           London
  Rainfall:       2.5 mm/h
  Alert Level:    GREEN
  Status:         Normal conditions
==================================================

==================================================
  RAINFALL MONITORING REPORT
==================================================
  City:           Tokyo
  Rainfall:       15.0 mm/h
  Alert Level:    YELLOW
  Status:         Moderate rainfall
==================================================

==================================================
  RAINFALL MONITORING REPORT
==================================================
  City:           Miami
  Rainfall:       0.0 mm/h
  Alert Level:    GREEN
  Status:         Normal conditions
==================================================
```

**Key features:**
- Graceful error handling: API failures return `0.0` instead of crashing
- Modular design: `monitor_city()` combines both functions
- Dictionary-based results for easy data handling
- Scalable: loop through any number of cities

Prompt4 Dashboard:
I am building a rainfall monitoring system using Python and Streamlit.

I already have:
- A function fetch_weather(city) that returns rainfall (mm/h)
- A function check_alert(rainfall) that returns (alert_level, message)

Please create a user-friendly Streamlit dashboard with a clean interface.

Requirements:

1. Layout and Title:
   - Display a centered title: "🌧️ Rainfall Monitor"
   - Add a subtitle: "Real-time rainfall monitoring and alert system"

2. User Input:
   - Add a text input for city name (default: "London")
   - Add a "Check Weather" button

3. Display Results in a clean layout:
   - Show rainfall using st.metric (large and clear)
   - Display alert level with color:
       GREEN → st.success()
       YELLOW → st.warning()
       RED → st.error()
   - Show a short message below the alert

4. Improve UI design:
   - Use spacing (st.write("") or st.markdown) to separate sections
   - Use emojis/icons to make it visually clear
   - Group results inside a container or columns

5. Behavior:
   - Only fetch data when the button is clicked
   - Handle errors gracefully (if API fails, show a warning message)

6. Optional (if simple to implement):
   - Add auto-refresh every 5 minutes
   - Display last updated time

7. Code quality:
   - Keep code clean and readable
   - Add comments explaining each part

Goal:
Create a simple, modern, and user-friendly dashboard.

# output:

After generating the dashboard code using AI (OpenCode), I reviewed the code quality and made several improvements.

First, I fixed warnings related to Streamlit components. For example, the parameter `use_container_width=True` was deprecated, so I replaced it with `width="stretch"` to ensure compatibility with future versions.

I also addressed warnings about empty labels in input fields by providing a proper label and hiding it using `label_visibility="collapsed"`, which improves accessibility without affecting the user interface.

In addition, I refined the user interface by adjusting layout spacing, improving text visibility on the dark background, and resizing the chart for better readability.

These changes helped make the application more robust, user-friendly, and aligned with good coding practices.