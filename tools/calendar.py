#!/usr/bin/env python3
"""Simple Calendar Tool for Harry-001"""

import json
import os
from pathlib import Path
from datetime import datetime, timedelta

CALENDAR_FILE = Path(os.path.expanduser("~/.config/harry_calendar.json"))

def load_calendar():
    if CALENDAR_FILE.exists():
        with open(CALENDAR_FILE) as f:
            return json.load(f)
    return {"events": []}

def save_calendar(data):
    os.makedirs(CALENDAR_FILE.parent, exist_ok=True)
    with open(CALENDAR_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def add_event(date, time, title, description=""):
    """Add event to calendar."""
    data = load_calendar()
    data["events"].append({
        "date": date,
        "time": time,
        "title": title,
        "description": description
    })
    data["events"].sort(key=lambda x: (x["date"], x["time"]))
    save_calendar(data)
    print(f"✅ Added: {date} {time} - {title}")

def view_today():
    """View today's events."""
    data = load_calendar()
    today = datetime.now().strftime("%Y-%m-%d")
    events = [e for e in data["events"] if e["date"] == today]
    
    print(f"\n📅 TODAY - {today}")
    print("="*30)
    if events:
        for e in events:
            print(f"  {e['time']} - {e['title']}")
            if e.get('description'):
                print(f"       {e['description']}")
    else:
        print("  No events scheduled")
    print()

def view_week():
    """View this week's events."""
    data = load_calendar()
    today = datetime.now()
    week_start = today - timedelta(days=today.weekday())
    
    print(f"\n📅 THIS WEEK - {week_start.strftime('%Y-%m-%d')} to {(week_start + timedelta(days=6)).strftime('%Y-%m-%d')}")
    print("="*30)
    
    for i in range(7):
        day = week_start + timedelta(days=i)
        day_str = day.strftime("%Y-%m-%d")
        day_name = day.strftime("%a %b %d")
        events = [e for e in data["events"] if e["date"] == day_str]
        
        print(f"\n{day_name}:")
        if events:
            for e in events:
                print(f"  {e['time']} - {e['title']}")
        else:
            print("  (Free)")
    print()

def main():
    import sys
    
    if len(sys.argv) < 2:
        print("📅 Harry-001 Calendar")
        print("Usage: python3 tools/calendar.py [command]")
        print("Commands:")
        print("  today        - View today's events")
        print("  week         - View this week's events")
        print("  add <date> <time> <title> [desc] - Add event")
        print("  list         - List all events")
        return
    
    cmd = sys.argv[1]
    
    if cmd == "today":
        view_today()
    elif cmd == "week":
        view_week()
    elif cmd == "add" and len(sys.argv) >= 5:
        add_event(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5] if len(sys.argv) > 5 else "")
    elif cmd == "list":
        data = load_calendar()
        for e in data["events"]:
            print(f"{e['date']} {e['time']} - {e['title']}")
    else:
        print("Unknown command")

if __name__ == "__main__":
    main()
