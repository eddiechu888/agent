# iPhone Notification Script

Python script to send push notifications to your iPhone using Pushover.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Install Pushover app on iPhone ($4.99)

3. Setup credentials:
```bash
python notify.py --setup
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