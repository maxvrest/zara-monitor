# 🚀 Quick Start Guide

Follow these steps to get your Zara Price Monitor up and running in 15 minutes!

## Step 1: Create Your Telegram Bot (5 min)

### 1.1 Open BotFather
1. Open Telegram on your phone or computer
2. Search for `@BotFather` (it's the official bot creation bot)
3. Click on it and press "Start"

### 1.2 Create Your Bot
1. Send the command: `/newbot`
2. BotFather will ask for a **name** - this can be anything, like "My Zara Monitor"
3. Then it asks for a **username** - must end in 'bot', like `my_zara_sales_bot`
4. **IMPORTANT**: Copy and save the **bot token** you receive!
   - It looks like: `1234567890:ABCdefGHIjklMNOpqrsTUVwxyz`
   - You'll need this later!

### 1.3 Get Your Chat ID
1. In Telegram, search for `@userinfobot`
2. Start a chat with it
3. It will send you your user info
4. **Copy your ID number** (looks like `123456789`)
5. Save this - it's your Chat ID!

### 1.4 Activate Your Bot
1. Search for your bot's username (the one you created in step 1.2)
2. Click "Start" to activate it
3. You can send it a test message like "Hello!"

✅ **Done!** You now have:
- Bot Token: `1234567890:ABC...`
- Chat ID: `123456789`

---

## Step 2: Install the Chrome Extension (3 min)

### 2.1 Download the Extension
1. Download this entire repository (green "Code" button → "Download ZIP")
2. Unzip it somewhere on your computer
3. Find the `extension` folder inside

### 2.2 Load in Chrome
1. Open Chrome
2. Type `chrome://extensions/` in the address bar and press Enter
3. Turn on **"Developer mode"** (toggle in top-right corner)
4. Click **"Load unpacked"**
5. Select the `extension` folder you found in step 2.1
6. The extension should now appear in your extensions list

### 2.3 Configure Extension
1. Click the puzzle icon in Chrome's toolbar
2. Find "Zara Price Monitor" and click it
3. Enter your **Chat ID** (from Step 1.3)
4. Click "Save Settings"

✅ **Done!** The extension is ready to use.

---

## Step 3: Set Up Automatic Monitoring (7 min)

This makes the monitoring run automatically every day, even when your computer is off.

### 3.1 Fork the Repository
1. Make sure you're logged into GitHub
2. Click the "Fork" button at the top-right of this repository page
3. Click "Create fork"
4. You now have your own copy!

### 3.2 Add Your Bot Token to GitHub
1. In YOUR forked repository, click **"Settings"** tab
2. In the left sidebar, click **"Secrets and variables"** → **"Actions"**
3. Click **"New repository secret"**
4. For "Name", type: `TELEGRAM_BOT_TOKEN`
5. For "Value", paste your bot token from Step 1.2
6. Click **"Add secret"**

⚠️ **Important**: This keeps your bot token secure. Never share it publicly!

### 3.3 Enable GitHub Actions
1. Click the **"Actions"** tab in your repository
2. Click the green button **"I understand my workflows, go ahead and enable them"**
3. You should see "Zara Price Monitor" workflow listed

### 3.4 Test It (Optional)
1. Still in the Actions tab, click **"Zara Price Monitor"**
2. Click **"Run workflow"** (dropdown)
3. Click the green **"Run workflow"** button
4. Wait a minute, then refresh - you should see a running workflow
5. Once it's done (green checkmark), it's working!

✅ **Done!** Your monitor will now run automatically every day at 9 AM CET.

---

## Step 4: Start Monitoring Products! (1 min)

### 4.1 Find a Product
1. Go to https://www.zara.com/nl/
2. Browse and find a product you like
3. Click on it to open the product detail page

### 4.2 Add to Monitoring
1. You should see a purple **"🔔 Monitor this product"** button on the page
2. Click it!
3. The button will turn green and say **"✓ Monitoring this product"**
4. You'll see a notification confirming it's added

### 4.3 View Your Monitored Products
1. Click the extension icon in Chrome
2. You'll see a list of all products you're monitoring
3. You can remove any product by clicking "Remove"

✅ **Done!** You're now monitoring your first product!

---

## 🎯 What Happens Next?

1. **Every day at 9 AM CET**, GitHub Actions will automatically:
   - Check the price of all your monitored products
   - Compare to the last known price
   
2. **If a price drops**, you'll get a Telegram message with:
   - Product name
   - Old price vs new price
   - Discount percentage
   - Link to buy it

3. **You don't need to do anything** - your computer can even be off!

---

## 🐛 Troubleshooting

### "I'm not seeing the button on Zara pages"
- Make sure you're on a **product detail page** (not category/search results)
- Try **refreshing the page**
- Check the extension is enabled in `chrome://extensions/`

### "I'm not getting notifications"
- Did you click "Start" in your bot's Telegram chat?
- Is your Chat ID correct in the extension settings?
- Did you add the bot token to GitHub secrets?
- Check the Actions tab - is the workflow running successfully?

### "The button clicked but nothing happened"
- Open the extension popup - is the product listed there?
- If yes, it's working! Notifications come only when prices drop.

### "GitHub Actions workflow is failing"
- Make sure `monitored_products.json` exists in your repository
- Check that `TELEGRAM_BOT_TOKEN` is spelled correctly in secrets
- Look at the error message in the workflow log

---

## 📱 Daily Usage

**Adding products**: Just click the button when browsing Zara  
**Checking monitored items**: Click the extension icon  
**Removing products**: Click "Remove" in the extension popup  
**Getting alerts**: Check your Telegram!

---

## 💰 Costs

Everything is **100% FREE**:
- ✅ Chrome extension: Free
- ✅ Telegram bot: Free
- ✅ GitHub Actions: Free (up to 2000 minutes/month - way more than needed)
- ✅ No credit card required anywhere

---

## 🎉 You're All Set!

Start adding products and wait for those sweet price drop notifications! 

Happy shopping! 🛍️

---

## Need Help?

Open an issue in this repository and I'll help you troubleshoot!
