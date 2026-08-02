# Instagram Following & Follower Checker

A Python script to find Instagram accounts you follow that don't follow you back.

## 📋 What It Does

- Parses your Instagram **Following** and **Followers** HTML exports
- Compares the two lists
- Outputs accounts you follow that **don't follow you back**
- Saves results to `not_following_back.txt`

## 🛠 Requirements

- Python 3.7+
- `beautifulsoup4` library

```bash
pip install beautifulsoup4
```

## 📥 How to Get Your Instagram Data

### Option 1: Browser DevTools (Recommended)

1. **Open Instagram** in your browser (desktop)
2. **Go to your profile** → Click **"Following"** (opens modal)
3. **Right-click inside the modal** → **Inspect Element**
4. In DevTools **Elements tab**, find the **scrollable container** holding the user list:
   - Look for a `div` with `role="dialog"` (the modal)
   - Inside it, find a `div` with `style="overflow: hidden auto"` or similar
   - This container has **many repeated child divs** (one per user)
5. **Scroll to bottom** in the modal to load ALL users
6. **Right-click the container** → **Copy → Copy outerHTML**
7. **Paste into `following.html`** in this project folder
8. **Repeat for "Followers"** → Paste into `follower.html`

### Option 2: Instagram Data Download

1. Go to Instagram Settings → **Your Activity** → **Download Your Information**
2. Request download → Wait for email
3. Extract `followers_and_following/followers_1.json` and `following.json`
4. Convert JSON to HTML format (requires additional script)

## 🚀 Usage

```bash
# Clone the repo
git clone https://github.com/DevThousif/Instagram-Following-and-Follower-CHECK.git
cd Instagram-Following-and-Follower-CHECK

# Install dependencies
pip install beautifulsoup4

# Add your HTML files (following.html & follower.html)

# Run the script
python main.py
```

## 📤 Output

- **Console**: Lists usernames not following you back
- **File**: `not_following_back.txt` - one username per line

```
tanjim.63_
afsarness
_saifbarakat_
atef_chy
...
```

## ⚠️ Important Notes

- **Class names change**: Instagram frequently updates CSS classes. The script uses flexible matching (`_ap3a _aaco` prefix) but may need updates.
- **Load all users**: Scroll to bottom in the modal before copying HTML, otherwise you'll only get the first ~12 users.
- **Private accounts**: This only works for accounts you can view (public or followed private accounts).
- **Rate limits**: Don't run too frequently - Instagram may block automated access.

## 🔧 Troubleshooting

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError: bs4` | Run `pip install beautifulsoup4` |
| `FileNotFoundError: following.html` | Create the file and paste your HTML |
| Only 12 users found | Scroll to bottom in modal before copying |
| Empty results | Verify HTML files contain user spans with `_ap3a _aaco` classes |
| Wrong users listed | Ensure you copied the scrollable container, not the whole page |

## 📁 Project Structure

```
Instagram-Following-and-Follower-CHECK/
├── main.py                 # Main script
├── following.html          # Paste your Following modal HTML here
├── follower.html           # Paste your Followers modal HTML here
├── not_following_back.txt  # Output (generated after run)
└── README.md               # This file
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

MIT License - feel free to use and modify.

## ⭐ Support

If this helps you, give it a star on GitHub!