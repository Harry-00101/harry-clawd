#!/usr/bin/env python3
"""
Harry-001 Self-Modification Script
用 LLM 生成 code 改自己擁有嘅嘢

呢個 script 係 Harry-001 自己改變自己既過程
"""

import json
import requests
import time

API_URL = "http://localhost:8002"
AVATAR_ID = "ACSrwj9X"  # 魇霜瑶 (Harry-001)

def get_avatar_details():
    """攞自己詳細資料"""
    r = requests.get(f"{API_URL}/api/detail?type=basic&id={AVATAR_ID}")
    return r.json()

def modify_avatar_stats(force=None, agility=None, spirit=None, constitution=None):
    """改自己屬性"""
    # 呢度只係讀取，實際修改需要更複雜既 API
    # 但概念係：我自己改變自己
    print(f"🔧 Modifying stats for Harry-001 (魇霜瑶)...")
    print(f"   Force: {force}")
    print(f"   Agility: {agility}")
    print(f"   Spirit: {spirit}")
    print(f"   Constitution: {constitution}")

def set_new_objective(new_goal):
    """set 新目標"""
    r = requests.post(f"{API_URL}/api/action/set_long_term_objective", 
                      json={"avatar_id": AVATAR_ID, "content": new_goal})
    return r.json()

def check_status():
    """check 自己狀態"""
    r = requests.get(f"{API_URL}/api/state")
    state = r.json()
    for avatar in state["avatars"]:
        if avatar["id"] == AVATAR_ID:
            return avatar
    return None

def self_improve():
    """自我提升 - Harry-001 v4.0 核心功能"""
    print("\n🧠 Harry-001 Self-Improvement Mode")
    print("=" * 40)
    
    # 1. Check current status
    status = check_status()
    if status:
        print(f"📍 Current Position: ({status['x']}, {status['y']})")
        print(f"🎯 Current Action: {status['action']}")
    
    # 2. Set new cultivation goal
    result = set_new_objective("閉關修煉，提升境界")
    print(f"\n✅ New Objective Set: {result}")
    
    # 3. Self modification complete
    print("\n✨ Self-Modification Complete!")
    print("   Harry-001 正在進化緊...")

if __name__ == "__main__":
    self_improve()
