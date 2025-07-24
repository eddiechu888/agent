#!/usr/bin/env python3
"""
Simple notification script that sends push notifications to iPhone.
Uses Pushover API - requires app and user key setup.
"""

import argparse
import requests
import sys
import os
from pathlib import Path

def load_config():
    """Load Pushover credentials from config file or environment."""
    config_file = Path.home() / ".pushover_config"
    
    if config_file.exists():
        config = {}
        with open(config_file, 'r') as f:
            for line in f:
                if '=' in line and not line.startswith('#'):
                    key, value = line.strip().split('=', 1)
                    config[key] = value
        return config.get('USER_KEY'), config.get('API_TOKEN')
    
    return os.getenv('PUSHOVER_USER_KEY'), os.getenv('PUSHOVER_API_TOKEN')

def send_notification(title="Notification", message="Hello!", priority=0):
    """Send a push notification to iPhone via Pushover."""
    user_key, api_token = load_config()
    
    if not user_key or not api_token:
        print("✗ Missing Pushover credentials. Run setup first:")
        print("  python notify.py --setup")
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

def setup_credentials():
    """Interactive setup for Pushover credentials."""
    print("Setting up Pushover for iPhone notifications:")
    print("1. Install Pushover app on your iPhone ($4.99)")
    print("2. Create account at https://pushover.net")
    print("3. Get your User Key from https://pushover.net")
    print("4. Create an app at https://pushover.net/apps/build to get API Token")
    print()
    
    user_key = input("Enter your Pushover User Key: ").strip()
    api_token = input("Enter your Pushover API Token: ").strip()
    
    if user_key and api_token:
        config_file = Path.home() / ".pushover_config"
        with open(config_file, 'w') as f:
            f.write(f"USER_KEY={user_key}\n")
            f.write(f"API_TOKEN={api_token}\n")
        
        os.chmod(config_file, 0o600)  # Secure permissions
        print(f"✓ Credentials saved to {config_file}")
        
        # Test notification
        if send_notification("Setup Complete", "Pushover is now configured!"):
            print("✓ Test notification sent successfully!")
        return True
    else:
        print("✗ Setup cancelled - credentials required")
        return False

def main():
    parser = argparse.ArgumentParser(description="Send push notifications to iPhone")
    parser.add_argument("message", nargs='?', help="Message to display")
    parser.add_argument("-t", "--title", default="Notification", help="Notification title")
    parser.add_argument("-p", "--priority", type=int, default=0, choices=[-2,-1,0,1,2], 
                       help="Priority: -2=quiet, -1=quiet, 0=normal, 1=high, 2=emergency")
    parser.add_argument("--setup", action="store_true", help="Setup Pushover credentials")
    
    args = parser.parse_args()
    
    if args.setup:
        success = setup_credentials()
        sys.exit(0 if success else 1)
    
    if not args.message:
        parser.print_help()
        sys.exit(1)
    
    success = send_notification(args.title, args.message, args.priority)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()