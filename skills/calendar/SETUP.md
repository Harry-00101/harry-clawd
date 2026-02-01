# Calendar Setup Guide

## Google Calendar Integration

### Prerequisites
1. Google Cloud account
2. OAuth 2.0 credentials

### Setup Steps

1. **Create OAuth Credentials:**
   - Go to: https://console.cloud.google.com/apis/credentials
   - Create OAuth 2.0 Client ID
   - Download JSON or copy credentials

2. **Set Environment Variables:**
   ```bash
   export GOOGLE_CLIENT_ID="your-client-id.apps.googleusercontent.com"
   export GOOGLE_CLIENT_SECRET="your-client-secret"
   export GOOGLE_REFRESH_TOKEN="your-refresh-token"
   ```

3. **Enable API:**
   - Enable Google Calendar API in Cloud Console

### Alternative: Simple Text Calendar

For now, use a simple text-based calendar:

**File:** `~/.config/harry_calendar.json`
```json
{
  "events": [
    {
      "date": "2026-02-01",
      "time": "09:00",
      "title": "Morning routine",
      "description": "Check weather, calendar, market"
    }
  ]
}
```

### Commands
```bash
# Add event
python3 tools/calendar.py add "2026-02-01 14:00" "Meeting"

# View today
python3 tools/calendar.py today

# View week
python3 tools/calendar.py week
```
