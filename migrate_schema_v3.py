"""
migrate_schema_v3.py -- Safe migration: checks column existence before adding.
Run ONCE: python migrate_schema_v3.py
"""
from dotenv import load_dotenv
load_dotenv()
import pymysql, os

def get_conn():
    return pymysql.connect(
        host=os.environ.get("MYSQL_HOST", "localhost"),
        user=os.environ.get("MYSQL_USER", "root"),
        password=os.environ.get("MYSQL_PASSWORD", ""),
        port=int(os.environ.get("MYSQL_PORT", "3306")),
        database=os.environ.get("MYSQL_DATABASE", "price_comparison")
    )

def get_columns(cur, table):
    cur.execute(f"SHOW COLUMNS FROM `{table}`;")
    return {row[0] for row in cur.fetchall()}

def get_tables(cur):
    cur.execute("SHOW TABLES;")
    return {row[0] for row in cur.fetchall()}

conn = get_conn()
cur = conn.cursor()
print("\n=== Schema Migration v3 (Safe) ===\n")

tables = get_tables(cur)

# ── Fix search_history ────────────────────────────────────────────────────────
print("[1/2] Fixing search_history table...")
if 'search_history' in tables:
    cols = get_columns(cur, 'search_history')
    # Remove old incompatible columns
    for old_col in ['search_name', 'searched_at']:
        if old_col in cols:
            cur.execute(f"ALTER TABLE `search_history` DROP COLUMN `{old_col}`;")
            conn.commit()
            print(f"  [OK] Dropped old column: {old_col}")

    cols = get_columns(cur, 'search_history')  # refresh
    # Add required columns
    if 'user_id' not in cols:
        cur.execute("ALTER TABLE `search_history` ADD COLUMN `user_id` INT NOT NULL DEFAULT 0 AFTER `id`;")
        conn.commit()
        print("  [OK] Added: user_id")
    if 'search_query' not in cols:
        cur.execute("ALTER TABLE `search_history` ADD COLUMN `search_query` VARCHAR(255) NOT NULL DEFAULT '' AFTER `user_id`;")
        conn.commit()
        print("  [OK] Added: search_query")
    if 'results_count' not in cols:
        cur.execute("ALTER TABLE `search_history` ADD COLUMN `results_count` INT DEFAULT 0 AFTER `search_query`;")
        conn.commit()
        print("  [OK] Added: results_count")
    if 'created_at' not in cols:
        cur.execute("ALTER TABLE `search_history` ADD COLUMN `created_at` DATETIME AFTER `results_count`;")
        conn.commit()
        print("  [OK] Added: created_at")
else:
    cur.execute("""
        CREATE TABLE `search_history` (
            `id` INT AUTO_INCREMENT PRIMARY KEY,
            `user_id` INT NOT NULL DEFAULT 0,
            `search_query` VARCHAR(255) NOT NULL DEFAULT '',
            `results_count` INT DEFAULT 0,
            `created_at` DATETIME,
            INDEX `idx_sh_user` (`user_id`)
        ) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
    """)
    conn.commit()
    print("  [OK] Created search_history table from scratch")

# ── Fix users table ───────────────────────────────────────────────────────────
print("\n[2/2] Fixing users table...")
if 'users' in tables:
    cols = get_columns(cur, 'users')
    extra_cols = {
        'phone':        "ALTER TABLE `users` ADD COLUMN `phone` VARCHAR(20) AFTER `email`;",
        'is_admin':     "ALTER TABLE `users` ADD COLUMN `is_admin` TINYINT(1) DEFAULT 0;",
        'last_login':   "ALTER TABLE `users` ADD COLUMN `last_login` DATETIME;",
        'is_active':    "ALTER TABLE `users` ADD COLUMN `is_active` TINYINT(1) DEFAULT 1;",
    }
    for col, sql in extra_cols.items():
        if col not in cols:
            cur.execute(sql)
            conn.commit()
            print(f"  [OK] Added: users.{col}")
        else:
            print(f"  [--] Already exists: users.{col}")

# ── Widen TEXT columns ────────────────────────────────────────────────────────
print("\n[3/3] Widening TEXT columns...")
widen = [
    ("product_prices", "product_link", "ALTER TABLE `product_prices` MODIFY COLUMN `product_link` TEXT;"),
    ("products",       "image_url",    "ALTER TABLE `products` MODIFY COLUMN `image_url` TEXT;"),
    ("products",       "name",         "ALTER TABLE `products` MODIFY COLUMN `name` VARCHAR(500) NOT NULL;"),
    ("products",       "description",  "ALTER TABLE `products` MODIFY COLUMN `description` TEXT;"),
]
for table, col, sql in widen:
    if table in tables:
        try:
            cur.execute(sql)
            conn.commit()
            print(f"  [OK] {table}.{col} widened")
        except Exception as e:
            print(f"  [SKIP] {table}.{col}: {e}")

cur.close()
conn.close()

# ── Show final schemas ─────────────────────────────────────────────────────────
print("\n=== Verifying Final Schemas ===")
conn2 = get_conn()
with conn2.cursor() as c:
    for tbl in ['search_history', 'users']:
        c.execute(f"DESCRIBE `{tbl}`;")
        print(f"\n  [{tbl}]")
        for r in c.fetchall():
            print(f"    {r[0]:<25} {r[1]}")
conn2.close()
print("\n[DONE] Migration complete. Restart the app with: python run.py\n")
