#!/usr/bin/env python3
"""
Zara Price Monitor - Daily price checker
Checks monitored products and sends Telegram notifications when prices drop
"""

import json
import os
import requests
from datetime import datetime
from typing import List, Dict, Optional
import time

class ZaraMonitor:
    def __init__(self, telegram_bot_token: str):
        self.telegram_bot_token = telegram_bot_token
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        })
    
    def load_products(self) -> List[Dict]:
        """Load monitored products from JSON file"""
        if not os.path.exists('monitored_products.json'):
            return []
        
        with open('monitored_products.json', 'r') as f:
            return json.load(f)
    
    def save_products(self, products: List[Dict]):
        """Save monitored products to JSON file"""
        with open('monitored_products.json', 'w') as f:
            json.dump(products, f, indent=2)
    
    def get_product_price(self, product_url: str) -> Optional[float]:
        """Scrape current price from Zara product page"""
        try:
            response = self.session.get(product_url, timeout=10)
            response.raise_for_status()
            
            # Look for price in the HTML
            # Zara uses JSON-LD structured data
            import re
            
            # Try to find price in JSON-LD
            json_ld_pattern = r'<script type="application/ld\+json">(.*?)</script>'
            matches = re.findall(json_ld_pattern, response.text, re.DOTALL)
            
            for match in matches:
                try:
                    data = json.loads(match)
                    if isinstance(data, dict) and 'offers' in data:
                        price = data['offers'].get('price')
                        if price:
                            return float(price)
                except:
                    continue
            
            # Fallback: look for price in common class names
            price_patterns = [
                r'price-current__amount[^>]*>([0-9,.]+)',
                r'"price"\s*:\s*"?([0-9,.]+)',
                r'data-price="([0-9,.]+)"',
                r'class="money-amount__main">([0-9,.]+)'
            ]
            
            for pattern in price_patterns:
                match = re.search(pattern, response.text)
                if match:
                    price_str = match.group(1).replace(',', '.')
                    return float(price_str)
            
            return None
            
        except Exception as e:
            print(f"Error fetching price: {e}")
            return None
    
    def send_telegram_message(self, chat_id: str, message: str):
        """Send notification via Telegram"""
        url = f"https://api.telegram.org/bot{self.telegram_bot_token}/sendMessage"
        
        payload = {
            'chat_id': chat_id,
            'text': message,
            'parse_mode': 'HTML'
        }
        
        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            print(f"Notification sent to {chat_id}")
        except Exception as e:
            print(f"Error sending Telegram message: {e}")
    
    def check_prices(self):
        """Main function to check all monitored products"""
        products = self.load_products()
        
        if not products:
            print("No products to monitor")
            return
        
        print(f"Checking {len(products)} products...")
        updated = False
        
        for product in products:
            print(f"\nChecking: {product['productName']}")
            
            current_price = self.get_product_price(product['url'])
            
            if current_price is None:
                print(f"  ⚠️ Could not fetch price")
                continue
            
            old_price = product.get('currentPrice')
            product['lastChecked'] = datetime.now().isoformat()
            
            if old_price is None:
                # First time checking this product
                product['currentPrice'] = current_price
                product['originalPrice'] = current_price
                updated = True
                print(f"  💰 Price recorded: €{current_price:.2f}")
            elif current_price < old_price:
                # Price dropped!
                discount = ((old_price - current_price) / old_price) * 100
                
                message = f"""
🔔 <b>Price Drop Alert!</b>

<b>{product['productName']}</b>

💰 Old price: €{old_price:.2f}
🎉 New price: €{current_price:.2f}
📉 Discount: {discount:.1f}% OFF

<a href="{product['url']}">View product</a>
"""
                
                self.send_telegram_message(product['telegramChatId'], message)
                
                product['currentPrice'] = current_price
                updated = True
                print(f"  🎉 PRICE DROP: €{old_price:.2f} → €{current_price:.2f}")
            elif current_price > old_price:
                # Price increased
                product['currentPrice'] = current_price
                updated = True
                print(f"  📈 Price increased: €{old_price:.2f} → €{current_price:.2f}")
            else:
                print(f"  ✓ No change: €{current_price:.2f}")
            
            # Be nice to Zara's servers
            time.sleep(2)
        
        if updated:
            self.save_products(products)
            print("\n✅ Product data updated")

def main():
    # Get Telegram bot token from environment variable
    bot_token = os.environ.get('TELEGRAM_BOT_TOKEN')
    
    if not bot_token:
        print("Error: TELEGRAM_BOT_TOKEN environment variable not set")
        print("Please set it in your GitHub repository secrets")
        return
    
    monitor = ZaraMonitor(bot_token)
    monitor.check_prices()

if __name__ == '__main__':
    main()
