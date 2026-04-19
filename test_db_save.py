#!/usr/bin/env python
"""Test database saving of scraped products"""

import sys
sys.path.insert(0, '/price-c-system')

from app import create_app, db
from app.models import Product, ProductPrice

# Create app context
app = create_app()

with app.app_context():
    # Scrape and save products
    from scraper.amazon_scraper import scrape_amazon
    from scraper.flipkart_scraper import scrape_flipkart
    from scraper.croma_scraper import scrape_croma
    from datetime import datetime
    
    product_name = "samsung"
    print(f"\nSearching for: {product_name}")
    print("=" * 70)
    
    # Scrape from all websites
    amazon_products = scrape_amazon(product_name)
    flipkart_products = scrape_flipkart(product_name)
    croma_products = scrape_croma(product_name)
    
    print(f"Found: Amazon={len(amazon_products)}, Flipkart={len(flipkart_products)}, Croma={len(croma_products)}")
    
    # Combine and save
    scraper_results = [
        ('Amazon', amazon_products),
        ('Flipkart', flipkart_products),
        ('Croma', croma_products)
    ]
    
    saved_count = 0
    
    for website, products in scraper_results:
        for product_data in products:
            try:
                # Try to find existing product by name
                product = Product.query.filter_by(name=product_data['title']).first()
                
                if not product:
                    # Create new product
                    product = Product(
                        name=product_data['title'],
                        category='Electronics',
                        image_url=product_data.get('image'),
                        description=product_data.get('specs', 'Product from ' + website)
                    )
                    db.session.add(product)
                    db.session.flush()
                    print(f"  ✓ Created product: {product_data['title'][:60]}")
                
                # Add or update price for this website
                price_entry = ProductPrice.query.filter_by(
                    product_id=product.id,
                    website=website
                ).first()
                
                if price_entry:
                    price_entry.price = product_data['price']
                    price_entry.product_link = product_data.get('link')
                    price_entry.fetched_at = datetime.utcnow()
                    print(f"    - Updated {website} price: Rs {product_data['price']}")
                else:
                    price_entry = ProductPrice(
                        product_id=product.id,
                        website=website,
                        price=product_data['price'],
                        product_link=product_data.get('link')
                    )
                    db.session.add(price_entry)
                    print(f"    - Added {website} price: Rs {product_data['price']}")
                
                saved_count += 1
            except Exception as e:
                print(f"  ✗ Error: {e}")
    
    # Commit all changes
    db.session.commit()
    
    print("\n" + "=" * 70)
    print(f"✅ Saved {saved_count} products to database!")
    print("=" * 70)
    
    # Show what's in database
    print("\nProducts in database for 'Samsung':")
    samsung_products = Product.query.filter(Product.name.ilike('%samsung%')).all()
    for p in samsung_products[:5]:
        print(f"\n  Product: {p.name}")
        prices = ProductPrice.query.filter_by(product_id=p.id).all()
        for price in prices:
            print(f"    - {price.website}: Rs {price.price}")
    
    print(f"\nTotal Samsung products in DB: {len(samsung_products)}")
