# -*- coding: utf-8 -*-
"""
setup_mysql.py -- Run this once to set up your MySQL database for PriceScope Pro.
Usage: python setup_mysql.py
"""
import sys
import os
import io

# Force UTF-8 output on Windows
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

# Load .env first
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

import pymysql

MYSQL_USER     = os.environ.get("MYSQL_USER", "root")
MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD", "")
MYSQL_HOST     = os.environ.get("MYSQL_HOST", "localhost")
MYSQL_PORT     = int(os.environ.get("MYSQL_PORT", "3306"))
MYSQL_DATABASE = os.environ.get("MYSQL_DATABASE", "price_comparison")

print("=" * 55)
print("  PriceScope Pro - MySQL Setup")
print("=" * 55)
print(f"  Host     : {MYSQL_HOST}:{MYSQL_PORT}")
print(f"  User     : {MYSQL_USER}")
print(f"  Database : {MYSQL_DATABASE}")
print(f"  Password : {'(set)' if MYSQL_PASSWORD else '(EMPTY - check .env)'}")
print("=" * 55)

# ── Step 1: Test connection ───────────────────────────────────────────────────
print("\n[1/3] Testing MySQL connection...")
try:
    conn = pymysql.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        port=MYSQL_PORT,
        connect_timeout=5
    )
    print("      [OK] Connected to MySQL successfully!")
except pymysql.OperationalError as e:
    print(f"\n  [FAIL] Cannot connect to MySQL: {e}")
    print("\n  Fix:")
    print("  1. Make sure MySQL is running (check MySQL Workbench or Services)")
    print("  2. Edit your .env file and set the correct MYSQL_PASSWORD")
    print("  3. Run this script again: python setup_mysql.py")
    sys.exit(1)

# ── Step 2: Create database ───────────────────────────────────────────────────
print(f"\n[2/3] Creating database '{MYSQL_DATABASE}'...")
try:
    with conn.cursor() as cur:
        cur.execute(
            f"CREATE DATABASE IF NOT EXISTS `{MYSQL_DATABASE}` "
            f"CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
        )
        cur.execute(f"USE `{MYSQL_DATABASE}`;")
    conn.commit()
    print(f"      [OK] Database '{MYSQL_DATABASE}' ready!")
except Exception as e:
    print(f"  [FAIL] Could not create database: {e}")
    conn.close()
    sys.exit(1)
conn.close()

# ── Step 3: Create all tables via Flask-SQLAlchemy ───────────────────────────
print("\n[3/3] Creating all tables via Flask-SQLAlchemy...")
try:
    from app import create_app
    from app.models import db

    app = create_app('development')
    with app.app_context():
        db.create_all()
    print("      [OK] All tables created!")
except Exception as e:
    print(f"  [FAIL] Table creation failed: {e}")
    sys.exit(1)

# ── Done ──────────────────────────────────────────────────────────────────────
print("\n" + "=" * 55)
print("  [DONE] MySQL Setup Complete!")
print("=" * 55)
print(f"\n  Database  : {MYSQL_DATABASE}")
print("  Tables    : users, products, product_prices,")
print("              favorites, reviews, price_alerts,")
print("              search_history")
print("\n  Now start the app:  python run.py")
print("  Then visit          http://127.0.0.1:5000\n")
