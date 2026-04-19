"""
migrate_mysql.py — Apply schema fixes to the MySQL price_comparison database.
Widens: product_link (TEXT), image_url (TEXT), name (VARCHAR 500)
"""
from dotenv import load_dotenv
load_dotenv()
import pymysql, os

conn = pymysql.connect(
    host=os.environ.get("MYSQL_HOST", "localhost"),
    user=os.environ.get("MYSQL_USER", "root"),
    password=os.environ.get("MYSQL_PASSWORD", ""),
    port=int(os.environ.get("MYSQL_PORT", "3306")),
    database=os.environ.get("MYSQL_DATABASE", "price_comparison")
)

migrations = [
    ("product_prices", "product_link",
     "ALTER TABLE `product_prices` MODIFY COLUMN `product_link` TEXT;"),

    ("products", "image_url",
     "ALTER TABLE `products` MODIFY COLUMN `image_url` TEXT;"),

    ("products", "name",
     "ALTER TABLE `products` MODIFY COLUMN `name` VARCHAR(500) NOT NULL;"),

    ("products", "description",
     "ALTER TABLE `products` MODIFY COLUMN `description` TEXT;"),
]

print("\n=== MySQL Schema Migration ===")
with conn.cursor() as cur:
    for table, col, sql in migrations:
        try:
            cur.execute(sql)
            conn.commit()
            print(f"  [OK] {table}.{col} -> widened")
        except Exception as e:
            print(f"  [SKIP] {table}.{col}: {e}")

conn.close()
print("\n[DONE] Migration complete — restart the Flask app.\n")
