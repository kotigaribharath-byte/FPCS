"""
migrate_schema_v2.py -- Fix all MySQL schema mismatches between the model and the live DB.
Run ONCE: python migrate_schema_v2.py
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
cur = conn.cursor()

print("\n=== Schema Migration v2 ===\n")

migrations = [
    # Fix search_history: drop old columns, add new ones
    ("Drop old search_history.search_name",
     "ALTER TABLE `search_history` DROP COLUMN IF EXISTS `search_name`;"),
    ("Drop old search_history.searched_at",
     "ALTER TABLE `search_history` DROP COLUMN IF EXISTS `searched_at`;"),
    ("Add search_history.user_id",
     "ALTER TABLE `search_history` ADD COLUMN IF NOT EXISTS `user_id` INT NOT NULL AFTER `id`;"),
    ("Add search_history.search_query",
     "ALTER TABLE `search_history` ADD COLUMN IF NOT EXISTS `search_query` VARCHAR(255) NOT NULL AFTER `user_id`;"),
    ("Add search_history.results_count",
     "ALTER TABLE `search_history` ADD COLUMN IF NOT EXISTS `results_count` INT DEFAULT 0 AFTER `search_query`;"),
    ("Add search_history.created_at",
     "ALTER TABLE `search_history` ADD COLUMN IF NOT EXISTS `created_at` DATETIME AFTER `results_count`;"),
    ("Add search_history FK index",
     "ALTER TABLE `search_history` ADD INDEX IF NOT EXISTS `idx_sh_user` (`user_id`);"),

    # Fix users: add missing columns the model expects
    ("Add users.is_admin",
     "ALTER TABLE `users` ADD COLUMN IF NOT EXISTS `is_admin` TINYINT(1) DEFAULT 0 AFTER `is_active`;"),
    ("Add users.phone",
     "ALTER TABLE `users` ADD COLUMN IF NOT EXISTS `phone` VARCHAR(20) AFTER `email`;"),
    ("Add users.is_active if missing",
     "ALTER TABLE `users` ADD COLUMN IF NOT EXISTS `is_active` TINYINT(1) DEFAULT 1;"),
    ("Add users.last_login",
     "ALTER TABLE `users` ADD COLUMN IF NOT EXISTS `last_login` DATETIME AFTER `updated_at`;"),

    # Widen existing columns (already done in v1, but safe to re-run)
    ("Widen product_prices.product_link -> TEXT",
     "ALTER TABLE `product_prices` MODIFY COLUMN `product_link` TEXT;"),
    ("Widen products.image_url -> TEXT",
     "ALTER TABLE `products` MODIFY COLUMN `image_url` TEXT;"),
    ("Widen products.name -> VARCHAR(500)",
     "ALTER TABLE `products` MODIFY COLUMN `name` VARCHAR(500) NOT NULL;"),
]

for label, sql in migrations:
    try:
        cur.execute(sql)
        conn.commit()
        print(f"  [OK]   {label}")
    except Exception as e:
        conn.rollback()
        print(f"  [SKIP] {label}: {str(e)[:80]}")

cur.close()
conn.close()

print("\n=== Final Table Schemas ===")
conn2 = pymysql.connect(
    host=os.environ.get("MYSQL_HOST", "localhost"),
    user=os.environ.get("MYSQL_USER", "root"),
    password=os.environ.get("MYSQL_PASSWORD", ""),
    port=int(os.environ.get("MYSQL_PORT", "3306")),
    database=os.environ.get("MYSQL_DATABASE", "price_comparison")
)
with conn2.cursor() as c:
    for table in ['search_history', 'users']:
        c.execute(f"DESCRIBE `{table}`;")
        rows = c.fetchall()
        print(f"\n  [{table}]")
        for r in rows:
            print(f"    {r[0]:<25} {r[1]}")
conn2.close()
print("\n[DONE] All schema fixes applied. Restart the app.\n")
