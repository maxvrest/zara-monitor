# 🔔 Zara Price Monitor

A Chrome extension and automated monitoring system that tracks Zara product prices and sends you Telegram notifications when items go on sale.

## ✨ Features

- **Chrome Extension**: Add a "Monitor this product" button on any Zara product page
- **Automatic Daily Checks**: Runs automatically in the cloud via GitHub Actions
- **Telegram Notifications**: Get instant alerts when prices drop
- **Works 24/7**: No need to keep your computer on
- **Netherlands Store**: Configured for Zara Netherlands

## 📋 Prerequisites

1. Google Chrome browser
2. GitHub account (free)
3. Telegram account

## 🚀 Setup Instructions

### Part 1: Create Telegram Bot (5 minutes)

1. **Open Telegram** and search for `@BotFather`

2. **Create a new bot**:
   - Send `/newbot`
   - Choose a name for your bot (e.g., "Zara Monitor")
   - Choose a username (e.g., "my_zara_monitor_bot")
   - **Save the bot token** you receive (looks like `123456789:ABCdefGHIjklMNOpqrsTUVwxyz`)

3. **Get your Chat ID**:
   - Search for `@userinfobot` in Telegram
   - Start a chat with it
   - **Save your Chat ID** (a number like `123456789`)

4. **Start your bot**:
   - Search for your bot's username in Telegram
   - Click "Start" to activate it

### Part 2: Install Chrome Extension (2 minutes)

1. **Download the extension**:
   - Download the `extension` folder from this repository

2. **Load in Chrome**:
   - Open Chrome and go to `chrome://extensions/`
   - Enable "Developer mode" (top right)
   - Click "Load unpacked"
   - Select the `extension` folder

3. **Configure the extension**:
   - Click the extension icon in Chrome
   - Enter your **Telegram Chat ID** from Part 1
   - Click "Save Settings"

### Part 3: Setup GitHub Actions (10 minutes)

This will enable automatic daily price checks even when your computer is off.

1. **Fork this repository**:
   - Click the "Fork" button at the top of this page
   - This creates your own copy

2. **Add your Telegram Bot Token**:
   - Go to your forked repository
   - Click "Settings" → "Secrets and variables" → "Actions"
   - Click "New repository secret"
   - Name: `TELEGRAM_BOT_TOKEN`
   - Value: Your bot token from Part 1 (step 2)
   - Click "Add secret"

3. **Enable GitHub Actions**:
   - Go to the "Actions" tab in your repository
   - Click "I understand my workflows, go ahead and enable them"

4. **Create the products file**:
   - In your repository, create a new file called `monitored_products.json`
   - Add this content: `[]`
   - Commit the file

5. **Test the workflow** (optional):
   - Go to "Actions" tab
   - Click "Zara Price Monitor" workflow
   - Click "Run workflow" → "Run workflow"
   - This will test that everything works

## 📱 How to Use

### Adding Products to Monitor

1. **Visit any Zara product page** (e.g., https://www.zara.com/nl/en/...)

2. **Click the "🔔 Monitor this product" button** that appears on the page

3. **That's it!** The product is now being monitored

### Managing Monitored Products

1. **Click the extension icon** in Chrome

2. **View your list** of monitored products

3. **Remove products** by clicking the "Remove" button

### Receiving Notifications

- You'll receive a Telegram message when any monitored product's price drops
- Messages include:
  - Product name
  - Old price
  - New price
  - Discount percentage
  - Link to the product

## ⏰ How Often Does It Check?

The system checks prices **once per day at 9 AM CET** (Netherlands time).

You can change this schedule in `.github/workflows/monitor.yml`:

```yaml
schedule:
  - cron: '0 8 * * *'  # 8 AM UTC = 9 AM CET
```

Cron schedule examples:
- `0 8 * * *` - Daily at 9 AM CET
- `0 8,20 * * *` - Twice daily: 9 AM and 9 PM CET
- `0 */6 * * *` - Every 6 hours

## 🛠 Advanced: Running Your Own API (Optional)

If you want to sync products across devices, you can deploy the API:

1. **Deploy to Render/Railway** (free tier):
   - Upload `api.py` and `requirements.txt`
   - Set environment variables
   - Get your API URL

2. **Update extension**:
   - In `popup.js`, replace `YOUR_API_ENDPOINT` with your API URL

## 📁 Project Structure

```
zara-monitor/
├── extension/              # Chrome extension
│   ├── manifest.json      # Extension config
│   ├── content.js         # Adds button to Zara pages
│   ├── popup.html         # Extension settings UI
│   ├── popup.js           # Settings logic
│   ├── background.js      # Background service worker
│   ├── styles.css         # Button styles
│   └── icons/             # Extension icons
├── .github/
│   └── workflows/
│       └── monitor.yml    # Daily monitoring schedule
├── monitor.py             # Price checking script
├── api.py                 # Optional API server
├── monitored_products.json # Your tracked products
└── requirements.txt       # Python dependencies
```

## 🔍 How It Works

1. **Extension** saves products to Chrome's local storage and GitHub repository
2. **GitHub Actions** runs `monitor.py` daily on GitHub's servers (free)
3. **Script** checks each product's current price
4. **If price drops**, sends you a Telegram notification
5. **Updates** the product data in the repository

## 🐛 Troubleshooting

### Extension not showing the button?
- Make sure you're on a Zara product detail page
- Try refreshing the page
- Check that the extension is enabled in `chrome://extensions/`

### Not receiving notifications?
- Make sure you started a chat with your bot in Telegram
- Verify your Chat ID is correct in extension settings
- Check that `TELEGRAM_BOT_TOKEN` is set in GitHub repository secrets
- Look at the Actions tab to see if the workflow is running

### GitHub Actions not running?
- Make sure you enabled Actions in your forked repository
- Check that `monitored_products.json` exists
- Verify the workflow file is in `.github/workflows/`

### Price not updating?
- Zara's website structure may have changed
- Open an issue with the product URL for debugging

## 📝 Requirements

Create `requirements.txt` with:

```
requests>=2.31.0
beautifulsoup4>=4.12.0
flask>=3.0.0
flask-cors>=4.0.0
```

## 🤝 Contributing

Found a bug? Have a feature request? Open an issue!

## 📄 License

MIT License - feel free to use and modify!

## ⚠️ Disclaimer

This tool is for personal use only. Please respect Zara's terms of service and don't abuse their servers. The script includes delays between requests to be respectful.

## 💡 Tips

- **Start small**: Monitor 5-10 products to start
- **Check regularly**: Review your monitored list and remove items you're no longer interested in
- **Sale seasons**: Add more products before sale seasons (January, July)
- **Size availability**: The extension tracks price, not size availability

## 🎉 Enjoy!

Happy shopping! May all your favorite Zara items go on sale! 🛍️
