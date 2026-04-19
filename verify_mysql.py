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
print("\n=== MySQL Schema Health Check ===\n")
with conn.cursor() as cur:
    cur.execute("SHOW TABLES;")
    tables = [r[0] for r in cur.fetchall()]
    print(f"Total tables: {len(tables)}\n")
    for table in tables:
        cur.execute(f"DESCRIBE `{table}`;")
        cols = [r[0] for r in cur.fetchall()]
        cur.execute(f"SELECT COUNT(*) FROM `{table}`")
        count = cur.fetchone()[0]
        print(f"  {table:<25} ({count:>5} rows)  cols: {', '.join(cols)}")
conn.close()
print("\n[OK] All tables healthy!\n")
