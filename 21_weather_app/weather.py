#!/usr/bin/env python3
"""
Weather App (uses OpenStreetMap Nominatim for geocoding and Open-Meteo for weather)
No API key required.
"""

import sys
from pathlib import Path

try:
    import requests
except Exception:
    print('This script requires the requests library. Install with: pip install requests')
    sys.exit(1)

NOMINATIM = 'https://nominatim.openstreetmap.org/search'
OPEN_METEO = 'https://api.open-meteo.com/v1/forecast'


def geocode(place: str):
    params = {'q': place, 'format': 'json', 'limit': 1}
    r = requests.get(NOMINATIM, params=params, headers={'User-Agent': 'python-projects'})
    r.raise_for_status()
    data = r.json()
    if not data:
        raise ValueError('Location not found')
    return float(data[0]['lat']), float(data[0]['lon'])


def fetch_weather(lat: float, lon: float):
    params = {'latitude': lat, 'longitude': lon, 'current_weather': 'true'}
    r = requests.get(OPEN_METEO, params=params)
    r.raise_for_status()
    return r.json().get('current_weather')


def main():
    if len(sys.argv) < 2:
        print('Usage: python weather.py "City name"')
        sys.exit(2)
    place = ' '.join(sys.argv[1:])
    try:
        lat, lon = geocode(place)
        weather = fetch_weather(lat, lon)
    except Exception as e:
        print('Error:', e)
        sys.exit(1)
    if not weather:
        print('No weather data available')
        return
    print(f"Location: {place} ({lat:.4f}, {lon:.4f})")
    print('Temperature:', weather.get('temperature'), '°C')
    print('Wind speed:', weather.get('windspeed'), 'm/s')
    print('Weather code:', weather.get('weathercode'))


if __name__ == '__main__':
    main()
