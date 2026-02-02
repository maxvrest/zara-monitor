#!/usr/bin/env python3
"""
Test script to verify your Telegram bot setup
"""

import os
import sys
import requests

def test_telegram_bot():
    print("🧪 Testing Telegram Bot Setup\n")
    
    # Get bot token
    bot_token = input("Enter your Telegram Bot Token: ").strip()
    if not bot_token:
        print("❌ Bot token is required!")
        return False
    
    # Get chat ID
    chat_id = input("Enter your Telegram Chat ID: ").strip()
    if not chat_id:
        print("❌ Chat ID is required!")
        return False
    
    print("\n📡 Testing bot connection...")
    
    # Test bot token
    try:
        response = requests.get(f"https://api.telegram.org/bot{bot_token}/getMe")
        if response.status_code == 200:
            bot_info = response.json()
            if bot_info['ok']:
                print(f"✅ Bot found: @{bot_info['result']['username']}")
            else:
                print(f"❌ Bot token invalid: {bot_info}")
                return False
        else:
            print(f"❌ Failed to connect to bot: Status {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Error connecting to Telegram: {e}")
        return False
    
    # Send test message
    print("\n📨 Sending test message...")
    try:
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        payload = {
            'chat_id': chat_id,
            'text': '🎉 Success! Your Zara Price Monitor is configured correctly!\n\nYou will receive notifications here when prices drop.'
        }
        response = requests.post(url, json=payload)
        
        if response.status_code == 200:
            result = response.json()
            if result['ok']:
                print("✅ Test message sent successfully!")
                print("\n🎉 Everything is working! Check your Telegram for the test message.")
                print("\n📝 Next steps:")
                print("1. Add your bot token to GitHub secrets as 'TELEGRAM_BOT_TOKEN'")
                print("2. Add your chat ID to the Chrome extension settings")
                print("3. Start monitoring products!")
                return True
            else:
                print(f"❌ Failed to send message: {result}")
                return False
        else:
            print(f"❌ Failed to send message: Status {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Error sending message: {e}")
        return False

if __name__ == '__main__':
    print("=" * 60)
    print("  Zara Price Monitor - Telegram Setup Test")
    print("=" * 60)
    print()
    
    success = test_telegram_bot()
    
    print("\n" + "=" * 60)
    if success:
        print("✅ ALL TESTS PASSED!")
    else:
        print("❌ TESTS FAILED - Please check the errors above")
        print("\n💡 Common issues:")
        print("   - Make sure you've started a chat with your bot in Telegram")
        print("   - Double-check your bot token and chat ID")
        print("   - Verify your bot token doesn't have extra spaces")
    print("=" * 60)
    
    sys.exit(0 if success else 1)
