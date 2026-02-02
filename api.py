#!/usr/bin/env python3
"""
Simple API server for Zara Monitor Extension
This is optional - the extension also works with just local storage
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

PRODUCTS_FILE = 'monitored_products.json'

def load_products():
    if os.path.exists(PRODUCTS_FILE):
        with open(PRODUCTS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_products(products):
    with open(PRODUCTS_FILE, 'w') as f:
        json.dump(products, f, indent=2)

@app.route('/monitor', methods=['POST'])
def add_product():
    """Add a product to monitoring"""
    data = request.json
    
    required_fields = ['productId', 'productName', 'url', 'telegramChatId']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400
    
    products = load_products()
    
    # Check if product already exists for this user
    existing = next((p for p in products 
                    if p['productId'] == data['productId'] 
                    and p['telegramChatId'] == data['telegramChatId']), None)
    
    if existing:
        return jsonify({'message': 'Product already monitored'}), 200
    
    # Add new product
    products.append(data)
    save_products(products)
    
    return jsonify({'message': 'Product added to monitoring'}), 201

@app.route('/monitor/<product_id>', methods=['DELETE'])
def remove_product(product_id):
    """Remove a product from monitoring"""
    chat_id = request.args.get('chatId')
    
    products = load_products()
    products = [p for p in products 
                if not (p['productId'] == product_id and p['telegramChatId'] == chat_id)]
    
    save_products(products)
    
    return jsonify({'message': 'Product removed'}), 200

@app.route('/monitor', methods=['GET'])
def get_products():
    """Get all monitored products for a user"""
    chat_id = request.args.get('chatId')
    
    if not chat_id:
        return jsonify({'error': 'chatId required'}), 400
    
    products = load_products()
    user_products = [p for p in products if p.get('telegramChatId') == chat_id]
    
    return jsonify(user_products), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
