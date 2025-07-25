# Agent Notification Instructions

## Send iPhone Notifications

Use this command to notify the user when tasks complete:

```bash
python3 ~/.local/bin/notify/notify.py "Your message here"
```

## Examples

**Task completion:**
```bash
python3 ~/.local/bin/notify/notify.py "Build completed successfully ✅" -t "Build Status"
```

**Error notifications:**
```bash
python3 ~/.local/bin/notify/notify.py "Build failed ❌" -t "Error" -p 1
```

**Critical alerts:**
```bash
python3 ~/.local/bin/notify/notify.py "Server down!" -t "CRITICAL" -p 2
```

## When to Use
- After long-running tasks (builds, tests, deployments)
- On task completion (success or failure)
- For important status updates
- When user attention is needed

## Priority Levels
- No flag: Normal priority
- `-p 1`: High priority (failures, important updates)
- `-p 2`: Emergency (critical alerts, bypasses quiet hours)
- `-p -1`: Quiet (low importance)

**Always use this command when completing significant tasks for the user.**