from scraper.flipkart_scraper import _get_fallback as fk, FLIPKART_PRODUCTS
from scraper.croma_scraper import _get_fallback as cr, CROMA_PRODUCTS
from scraper.amazon_scraper import _get_amazon_fallback as az, AMAZON_PRODUCTS

tests = [
    'samsung galaxy', 'iphone 16', 'laptop gaming', 'tv OLED', 'headphones ANC',
    'washing machine', 'camera mirrorless', 'ps5 gaming', 'router wifi', 'power bank',
    'vivo x200', 'oneplus 13', 'realme gt', 'poco x7', 'redmi note 14', 'monitor',
    'refrigerator', 'ac inverter', 'pixel 9', 'oppo reno'
]

print("\n=== CATALOG SEARCH TEST ===")
for t in tests:
    fk_res = fk(t)
    cr_res = cr(t)
    az_res = az(t)
    print(f"  [{t:22s}] Flipkart:{len(fk_res):2d} | Croma:{len(cr_res):2d} | Amazon:{len(az_res):2d}")

fk_total = sum(len(v) for v in FLIPKART_PRODUCTS.values())
cr_total = sum(len(v) for v in CROMA_PRODUCTS.values())
az_total = sum(len(v) for v in AMAZON_PRODUCTS.values())
grand = fk_total + cr_total + az_total
print(f"\n=== CATALOG SIZE ===")
print(f"  Flipkart : {fk_total} products across {len(FLIPKART_PRODUCTS)} categories")
print(f"  Croma    : {cr_total} products across {len(CROMA_PRODUCTS)} categories")
print(f"  Amazon   : {az_total} products across {len(AMAZON_PRODUCTS)} categories")
print(f"  TOTAL    : {grand} product entries across all stores")
print("\n=== CATEGORIES COVERED ===")
all_keys = set(list(FLIPKART_PRODUCTS.keys()) + list(CROMA_PRODUCTS.keys()) + list(AMAZON_PRODUCTS.keys()))
for k in sorted(all_keys):
    print(f"  - {k}")
