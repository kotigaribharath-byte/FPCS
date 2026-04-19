#!/usr/bin/env python
"""Show updated products"""

from scraper.flipkart_scraper import SAMPLE_FLIPKART_PRODUCTS
from scraper.croma_scraper import SAMPLE_CROMA_PRODUCTS

print("\n" + "="*70)
print("LATEST 2025-2026 PRODUCTS NOW AVAILABLE")
print("="*70)

print("\n--- SAMSUNG (Flipkart Fallback Data) ---")
for p in SAMPLE_FLIPKART_PRODUCTS['samsung'][:4]:
    print(f"  • {p['title']}")
    print(f"    Price: Rs {p['price']} | Rating: {p['rating']} ({p['reviews']} reviews)")

print("\n--- IPHONE (Flipkart Fallback Data) ---")
for p in SAMPLE_FLIPKART_PRODUCTS['iphone'][:4]:
    print(f"  • {p['title']}")
    print(f"    Price: Rs {p['price']} | Rating: {p['rating']} ({p['reviews']} reviews)")

print("\n--- LAPTOP (Flipkart Fallback Data) ---")
for p in SAMPLE_FLIPKART_PRODUCTS['laptop'][:4]:
    print(f"  • {p['title']}")
    print(f"    Price: Rs {p['price']} | Rating: {p['rating']} ({p['reviews']} reviews)")

print("\n--- REALME (Latest 2025) ---")
for p in SAMPLE_FLIPKART_PRODUCTS['realme'][:4]:
    print(f"  • {p['title']}")
    print(f"    Price: Rs {p['price']} | Rating: {p['rating']} ({p['reviews']} reviews)")

print("\n--- SMARTWATCH (New Category) ---")
for p in SAMPLE_FLIPKART_PRODUCTS['watch'][:3]:
    print(f"  • {p['title']}")
    print(f"    Price: Rs {p['price']} | Rating: {p['rating']} ({p['reviews']} reviews)")

print("\n" + "="*70)
print("✅ All products updated with latest 2025-2026 models!")
print("="*70 + "\n")
