# 21_weather_app

Fetch current weather for a place using free public services (OpenStreetMap + Open-Meteo). No API key required.

Usage:
- pip install -r requirements.txt
- python weather.py "New York"

Notes:
- Uses Nominatim for geocoding; respect usage policy and rate limits.

Possible improvement:
- Map Open-Meteo weather codes to human-friendly descriptions and add a 3-day forecast option.
