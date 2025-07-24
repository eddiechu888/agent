# iPhone Notification Script

Python script to send push notifications to your iPhone using Pushover (30-day free trial).

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Install Pushover app on iPhone (free 30-day trial)

3. Get credentials from https://pushover.net:
   - Sign up and get your User Key
   - Create an app to get API Token

4. Setup environment:
```bash
cp .env.example .env
# Edit .env with your credentials
```

## Usage

```bash
# Basic notification
python notify.py "Your message here"

# With custom title
python notify.py "Your message" -t "Custom Title"

# With priority (emergency notifications)
python notify.py "Urgent!" -p 2

# Quiet notification
python notify.py "FYI" -p -1
```

Priority levels:
- `-2`: No notification/badge only
- `-1`: Quiet notification
- `0`: Normal priority (default)
- `1`: High priority
- `2`: Emergency (bypasses quiet hours, repeats until acknowledged)