#!/usr/bin/env python3
"""
Simple notification script that sends push notifications to iPhone using Pushover.
Uses .env file for secure credential storage.
"""

import argparse
import requests
import sys
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_pushover_credentials():
    """Get Pushover credentials from environment variables."""
    user_key = os.getenv('PUSHOVER_USER_KEY')
    api_token = os.getenv('PUSHOVER_API_TOKEN')
    return user_key, api_token

def send_notification(title="Notification", message="Hello!", priority=0):
    """Send a push notification to iPhone via Pushover."""
    user_key, api_token = get_pushover_credentials()
    
    if not user_key or not api_token:
        print("✗ Missing Pushover credentials.")
        print("1. Copy .env.example to .env")
        print("2. Add your Pushover credentials to .env")
        print("3. Get credentials from https://pushover.net")
        return False
    
    try:
        response = requests.post("https://api.pushover.net/1/messages.json", data={
            "token": api_token,
            "user": user_key,
            "title": title,
            "message": message,
            "priority": priority
        })
        
        if response.status_code == 200:
            print(f"✓ Notification sent to iPhone: {title}")
            return True
        else:
            print(f"✗ Failed to send notification: {response.json()}")
            return False
            
    except Exception as e:
        print(f"✗ Failed to send notification: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Send push notifications to iPhone")
    parser.add_argument("message", help="Message to display")
    parser.add_argument("-t", "--title", default="Notification", help="Notification title")
    parser.add_argument("-p", "--priority", type=int, default=0, choices=[-2,-1,0,1,2], 
                       help="Priority: -2=quiet, -1=quiet, 0=normal, 1=high, 2=emergency")
    
    args = parser.parse_args()
    
    success = send_notification(args.title, args.message, args.priority)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()