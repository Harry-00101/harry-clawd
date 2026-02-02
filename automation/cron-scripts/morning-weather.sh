#!/bin/bash
# Morning Weather Check - Runs at 07:00 HKT
cd /root/clawd
python3 -c "
import urllib.request, json
url = 'https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrread&lang=tc'
try:
    with urllib.request.urlopen(url, timeout=10) as resp:
        data = json.loads(resp.read().decode())
        temp = data.get('temperature', {}).get('data', [{}])[0].get('value', 'N/A')
        print(f'🌡️ HK Temperature: {temp}°C')
except Exception as e:
    print(f'Weather check: {e}')
"
echo "Morning weather check complete"
