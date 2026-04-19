#!/usr/bin/env python
"""Test the comparison endpoint and database saving"""

import requests
import time

BASE_URL = "http://127.0.0.1:5000"

print("\n" + "="*70)
print("TESTING PRODUCT COMPARISON WITH DATABASE SAVING")
print("="*70)

# Test search
search_query = "iphone"
print(f"\nSearching for: '{search_query}'")
print(f"URL: {BASE_URL}/products/compare?q={search_query}")

try:
    response = requests.get(f"{BASE_URL}/products/compare?q={search_query}", timeout=60)
    
    if response.status_code == 200:
        print(f"✅ Status: {response.status_code}")
        
        # Check if products are in the response
        if "Samsung Galaxy" in response.text or "iPhone" in response.text:
            print(f"✅ Products found in response")
        
        if "Amazon" in response.text or "Flipkart" in response.text or "Croma" in response.text:
            print(f"✅ Multiple stores detected in response")
            
        # Count mentions of websites
        amazon_count = response.text.count("Amazon")
        flipkart_count = response.text.count("Flipkart")
        croma_count = response.text.count("Croma")
        
        print(f"\nWebsite mentions in response:")
        print(f"  - Amazon: {amazon_count} times")
        print(f"  - Flipkart: {flipkart_count} times")
        print(f"  - Croma: {croma_count} times")
    else:
        print(f"❌ Status: {response.status_code}")
        print(response.text[:500])
except Exception as e:
    print(f"❌ Error: {e}")

print("\n" + "="*70)
print("CHECKING DATABASE FOR SAVED PRODUCTS")
print("="*70)

from app import create_app, db
from app.models import Product, ProductPrice

app = create_app()

with app.app_context():
    total_products = Product.query.count()
    total_prices = ProductPrice.query.count()
    
    print(f"\n✅ Database Status:")
    print(f"   - Total Products Stored: {total_products}")
    print(f"   - Total Price Entries: {total_prices}")
    
    # Show recent products
    print(f"\nRecent Products Added:")
    recent = Product.query.order_by(Product.created_at.desc()).limit(5).all()
    for p in recent:
        prices = ProductPrice.query.filter_by(product_id=p.id).all()
        print(f"  • {p.name[:60]}")
        for price in prices:
            print(f"     - {price.website}: Rs {price.price}")

print("\n" + "="*70)
