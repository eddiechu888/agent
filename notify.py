#!/usr/bin/env python3
"""
Simple notification script that can send desktop notifications.
Uses plyer for cross-platform notifications - works on macOS, Windows, Linux.
"""

import argparse
from plyer import notification
import sys

def send_notification(title="Notification", message="Hello!", timeout=5):
    """Send a desktop notification."""
    try:
        notification.notify(
            title=title,
            message=message,
            timeout=timeout
        )
        print(f"✓ Notification sent: {title}")
        return True
    except Exception as e:
        print(f"✗ Failed to send notification: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Send desktop notifications")
    parser.add_argument("message", help="Message to display")
    parser.add_argument("-t", "--title", default="Notification", help="Notification title")
    parser.add_argument("--timeout", type=int, default=5, help="Timeout in seconds")
    
    args = parser.parse_args()
    
    success = send_notification(args.title, args.message, args.timeout)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()