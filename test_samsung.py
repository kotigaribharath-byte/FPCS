#!/usr/bin/env python
"""Test Samsung product search"""

from scraper.flipkart_scraper import scrape_flipkart
from scraper.croma_scraper import scrape_croma
from scraper.amazon_scraper import scrape_amazon

print("Testing Samsung product search with updated products...")
print("=" * 60)

flipkart = scrape_flipkart('samsung')
croma = scrape_croma('samsung')
amazon = scrape_amazon('samsung')

print(f'\nFlipkart Samsung products: {len(flipkart)}')
for i, p in enumerate(flipkart[:3], 1):
    title = p['title'][:70]
    price = p['price']
    rating = p.get('rating', 'N/A')
    print(f'  {i}. {title} | Rs {price} | Rating: {rating}')

print(f'\nCroma Samsung products: {len(croma)}')
for i, p in enumerate(croma[:3], 1):
    title = p['title'][:70]
    price = p['price']
    rating = p.get('rating', 'N/A')
    print(f'  {i}. {title} | Rs {price} | Rating: {rating}')

print(f'\nAmazon Samsung products: {len(amazon)}')
for i, p in enumerate(amazon[:3], 1):
    title = p['title'][:70]
    price = p['price']
    rating = p.get('rating', 'N/A')
    print(f'  {i}. {title} | Rs {price} | Rating: {rating}')

print(f'\n✅ Total products found: {len(flipkart) + len(croma) + len(amazon)}')
