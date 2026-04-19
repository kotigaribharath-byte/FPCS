import sys
sys.path.insert(0, 'd:/price-c-system')
from scraper.amazon_scraper import scrape_amazon
from scraper.flipkart_scraper import scrape_flipkart
from scraper.croma_scraper import scrape_croma

query = "samsung"
print("=== AMAZON ===")
a = scrape_amazon(query)
for p in a[:2]:
    print(f"  {p.get('title','')[:50]} | IMG: {str(p.get('image',''))[:60]}")

print(f"\n=== FLIPKART ({len(a)} amazon results) ===")
f = scrape_flipkart(query)
for p in f[:2]:
    print(f"  {p.get('title','')[:50]} | IMG: {str(p.get('image',''))[:60]}")

print(f"\n=== CROMA ===")
c = scrape_croma(query)
for p in c[:2]:
    print(f"  {p.get('title','')[:50]} | IMG: {str(p.get('image',''))[:60]}")

print(f"\nTOTAL: Amazon={len(a)}, Flipkart={len(f)}, Croma={len(c)}")
