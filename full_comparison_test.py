#!/usr/bin/env python
"""Full comparison test"""

from scraper.flipkart_scraper import scrape_flipkart
from scraper.croma_scraper import scrape_croma
from scraper.amazon_scraper import scrape_amazon

print("\n" + "="*70)
print("FULL PRODUCT COMPARISON - SAMSUNG")
print("="*70)

flipkart = scrape_flipkart('samsung')
croma = scrape_croma('samsung')
amazon = scrape_amazon('samsung')

print(f"\nFlipkart: {len(flipkart)} products")
for i, p in enumerate(flipkart[:3], 1):
    print(f"  {i}. {p['title'][:60]}")
    print(f"     Price: Rs {p['price']} | Rating: {p.get('rating', 'N/A')}")

print(f"\nCroma: {len(croma)} products")
for i, p in enumerate(croma[:3], 1):
    print(f"  {i}. {p['title'][:60]}")
    print(f"     Price: Rs {p['price']} | Rating: {p.get('rating', 'N/A')}")

print(f"\nAmazon: {len(amazon)} products")
for i, p in enumerate(amazon[:3], 1):
    print(f"  {i}. {p['title'][:60]}")
    print(f"     Price: Rs {p['price']} | Rating: {p.get('rating', 'N/A')}")

total = len(flipkart) + len(croma) + len(amazon)
print("\n" + "="*70)
print(f"✅ TOTAL: {total} products found across all stores!")
print("="*70 + "\n")
