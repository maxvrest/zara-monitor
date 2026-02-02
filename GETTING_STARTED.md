# 🎯 Getting Started - Zara Price Monitor

## What You've Got

A complete Zara price monitoring system with:
- ✅ Chrome extension with one-click product monitoring
- ✅ Automated daily price checks (runs in the cloud)
- ✅ Telegram notifications for price drops
- ✅ Works 24/7 even when your MacBook is off
- ✅ 100% free to run

## 🚀 Three Simple Steps to Get Started

### Step 1: Set Up Telegram (5 minutes)
1. Open Telegram and message `@BotFather`
2. Send `/newbot` and follow the prompts
3. **Save your bot token** (looks like `123456:ABC...`)
4. Message `@userinfobot` to get your Chat ID
5. **Save your Chat ID** (a number like `123456789`)

📖 **Detailed guide**: See `QUICKSTART.md` in the project folder

### Step 2: Install Chrome Extension (2 minutes)
1. Open Chrome → `chrome://extensions/`
2. Enable "Developer mode" (top right)
3. Click "Load unpacked"
4. Select the `extension` folder
5. Click the extension icon and enter your Chat ID

### Step 3: Set Up GitHub Actions (8 minutes)
1. Fork this repository on GitHub
2. Add `TELEGRAM_BOT_TOKEN` to repository secrets
3. Enable GitHub Actions in the Actions tab
4. Done! It will check prices daily at 9 AM CET

📖 **Detailed guide**: See `QUICKSTART.md` in the project folder

## 📱 How to Use

1. **Visit any Zara product page** in the Netherlands store
2. **Click the purple "Monitor this product" button** that appears
3. **Wait for notifications** when prices drop!

That's it! The system does everything else automatically.

## 🎁 What's Included

```
📦 zara-monitor/
   ├── 📱 extension/           → Chrome extension (ready to use)
   ├── 🤖 monitor.py           → Price checking script
   ├── ⚙️  .github/workflows/  → Automated scheduling
   ├── 📚 README.md            → Full documentation
   ├── 🚀 QUICKSTART.md        → Step-by-step setup
   ├── 🧪 test_telegram.py     → Test your setup
   └── 📋 requirements.txt     → Dependencies
```

## 🧪 Test Your Setup

Before adding products, test your Telegram connection:

```bash
python test_telegram.py
```

This will:
- Verify your bot token
- Send a test message
- Confirm everything works

## ⚙️ Customization

### Change Check Frequency
Edit `.github/workflows/monitor.yml`:
- `0 8 * * *` = Daily at 9 AM CET (current)
- `0 8,20 * * *` = Twice daily (9 AM & 9 PM)
- `0 */6 * * *` = Every 6 hours

### Notification Format
Edit `monitor.py` to customize the Telegram message format.

### Monitor Multiple Stores
The extension currently works for Zara Netherlands. To add other countries:
- Update `manifest.json` host permissions
- Modify `content.js` URL matching

## 💰 Costs

**Everything is FREE:**
- Chrome extension: Free
- Telegram bot: Free  
- GitHub Actions: Free (2000 min/month included)
- No credit card needed anywhere

## 🆘 Need Help?

1. **Read QUICKSTART.md** for detailed setup steps
2. **Run test_telegram.py** to verify your configuration
3. **Check README.md** for troubleshooting tips
4. **Open an issue** on GitHub if you're stuck

## 🎉 You're Ready!

1. ✅ Follow the 3 setup steps above
2. ✅ Add products you're interested in
3. ✅ Relax and wait for price drop notifications!

Happy shopping! 🛍️

---

**Need help?** Check QUICKSTART.md for detailed instructions with screenshots!
