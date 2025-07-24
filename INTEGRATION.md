# Using notify.py in Other Projects

## Option 1: Global Installation (Recommended)

1. **Create a global notifications directory:**
```bash
mkdir -p ~/.local/bin/notify
cd ~/.local/bin/notify
```

2. **Copy files:**
```bash
cp /path/to/this/project/notify.py ~/.local/bin/notify/
cp /path/to/this/project/.env ~/.local/bin/notify/
cp /path/to/this/project/requirements.txt ~/.local/bin/notify/
```

3. **Install dependencies:**
```bash
cd ~/.local/bin/notify
pip install -r requirements.txt
```

4. **Make it executable and add to PATH:**
```bash
chmod +x ~/.local/bin/notify/notify.py
echo 'export PATH="$HOME/.local/bin/notify:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

5. **Test from anywhere:**
```bash
cd /any/project
python ~/.local/bin/notify/notify.py "Build complete!"
```

## Option 2: Per-Project Installation

1. **Copy files to your project:**
```bash
cp notify.py /path/to/your/project/
cp .env /path/to/your/project/
```

2. **Add to project's requirements.txt:**
```txt
requests==2.31.0
python-dotenv==1.0.0
```

3. **Use in project:**
```bash
python notify.py "Task completed!"
```

## Windsurf Integration Commands

### Basic Usage
```bash
# Simple notification
python ~/.local/bin/notify/notify.py "Build finished!"

# With custom title
python ~/.local/bin/notify/notify.py "All tests passed ✅" -t "Test Results"

# High priority for errors
python ~/.local/bin/notify/notify.py "Build failed!" -t "Error" -p 1

# Emergency for critical issues
python ~/.local/bin/notify/notify.py "Server down!" -t "CRITICAL" -p 2
```

### Common Windsurf Scenarios

**After successful build:**
```bash
npm run build && python ~/.local/bin/notify/notify.py "Build completed successfully ✅" -t "Build Status"
```

**After tests:**
```bash
npm test && python ~/.local/bin/notify/notify.py "All tests passed ✅" -t "Test Results" || python ~/.local/bin/notify/notify.py "Tests failed ❌" -t "Test Results" -p 1
```

**After deployment:**
```bash
./deploy.sh && python ~/.local/bin/notify/notify.py "Deployment successful 🚀" -t "Deployment"
```

**Long-running tasks:**
```bash
# Start notification
python ~/.local/bin/notify/notify.py "Starting data processing..." -t "Task Started"
# ... your long task ...
python process_data.py
# Completion notification
python ~/.local/bin/notify/notify.py "Data processing complete!" -t "Task Finished"
```

## Quick Command Reference

| Command | Description |
|---------|-------------|
| `python ~/.local/bin/notify/notify.py "message"` | Basic notification |
| `python ~/.local/bin/notify/notify.py "msg" -t "Title"` | With custom title |
| `python ~/.local/bin/notify/notify.py "msg" -p 1` | High priority |
| `python ~/.local/bin/notify/notify.py "msg" -p 2` | Emergency (bypasses quiet hours) |
| `python ~/.local/bin/notify/notify.py "msg" -p -1` | Quiet notification |

## Pro Tips

- Use priority `-1` for low-importance notifications
- Use priority `1` for build failures or important updates  
- Use priority `2` for critical alerts that need immediate attention
- Keep messages under 1024 characters for best results
- Test with a simple message first: `python ~/.local/bin/notify/notify.py "test"`