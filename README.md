# Notification Script

Simple Python script to send desktop notifications.

## Setup

```bash
pip install -r requirements.txt
```

## Usage

```bash
# Basic notification
python notify.py "Your message here"

# With custom title
python notify.py "Your message" -t "Custom Title"

# With timeout
python notify.py "Your message" --timeout 10
```