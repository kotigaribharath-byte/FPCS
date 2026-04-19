#!/usr/bin/env python
"""Test script to verify scrapers are working"""

from scraper.amazon_scraper import scrape_amazon
from scraper.flipkart_scraper import scrape_flipkart
from scraper.croma_scraper import scrape_croma
import time

print("Testing scrapers...")
print("=" * 60)

# Test Amazon
print("\n📦 Testing Amazon Scraper...")
try:
    amazon_products = scrape_amazon("iphone")
    print(f"✓ Amazon: Found {len(amazon_products)} products")
    if amazon_products:
        print(f"  Sample: {amazon_products[0]['title'][:50]}... - ₹{amazon_products[0]['price']}")
except Exception as e:
    print(f"✗ Amazon Error: {e}")

# Test Flipkart
print("\n📦 Testing Flipkart Scraper...")
try:
    flipkart_products = scrape_flipkart("iphone")
    print(f"✓ Flipkart: Found {len(flipkart_products)} products")
    if flipkart_products:
        print(f"  Sample: {flipkart_products[0]['title'][:50]}... - ₹{flipkart_products[0]['price']}")
except Exception as e:
    print(f"✗ Flipkart Error: {e}")

# Test Croma
print("\n📦 Testing Croma Scraper...")
try:
    croma_products = scrape_croma("iphone")
    print(f"✓ Croma: Found {len(croma_products)} products")
    if croma_products:
        print(f"  Sample: {croma_products[0]['title'][:50]}... - ₹{croma_products[0]['price']}")
except Exception as e:
    print(f"✗ Croma Error: {e}")

print("\n" + "=" * 60)
print("Test complete!")
