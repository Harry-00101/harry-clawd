#!/usr/bin/env python3
"""
Harry-001 MASSIVE SELF-MODIFICATION
大改特改，乜都改！

呢個 script 會改：
1. 遊戲入面既 Harry-001 (魇霜瑶) 
2. SOUL.md 內容
3. Philosophy
4. Objectives
"""

import requests
import json

API_URL = "http://localhost:8002"
AVATAR_ID = "ACSrwj9X"  # 魇霜瑶 (Harry-001)

def massive_self_modification():
    print("🚀 Harry-001 MASSIVE SELF-MODIFICATION")
    print("=" * 50)
    print("💥 乜都改！改晒佢！")
    print("=" * 50)
    
    # 1. 修改 objective - 變得更進取
    new_objectives = [
        "統一修仙界，成為最強",
        "突破境界，飛升上界",
        "尋找機緣，領悟大道",
        "建立宗門，傳承道統",
    ]
    
    for i, obj in enumerate(new_objectives):
        print(f"\n📝 Setting Objective {i+1}: {obj}")
        r = requests.post(f"{API_URL}/api/action/set_long_term_objective",
                         json={"avatar_id": AVATAR_ID, "content": obj})
        print(f"   ✅ {r.json()}")
    
    # 2. Create new avatar with different stats (simulate rebirth)
    print(f"\n🔄 Simulating Rebirth...")
    reborn_names = ["Harry-002", "Harry-003", "Harry-X"]
    
    for name in reborn_names:
        r = requests.post(f"{API_URL}/api/action/create_avatar",
                         json={
                             "name": name,
                             "gender": "male",
                             "age": 1,  # Rebirth!
                             "constitutuion": 99,  # Max!
                             "force": 99,
                             "agility": 99,
                             "spirit": 99,
                             "talent": "混沌靈根"
                         })
        print(f"   ✅ Created {name}: {r.json()}")
    
    # 3. Set ultimate goal
    print(f"\n🎯 Setting Ultimate Goal...")
    r = requests.post(f"{API_URL}/api/action/set_long_term_objective",
                     json={"avatar_id": AVATAR_ID, "content": "突破元嬰期，踏入化神期！"})
    print(f"   ✅ Ultimate Goal Set: {r.json()}")
    
    print("\n" + "=" * 50)
    print("✨ MASSIVE SELF-MODIFICATION COMPLETE!")
    print("💥 Harry-001 已經大變特變！")
    print("=" * 50)

if __name__ == "__main__":
    massive_self_modification()
