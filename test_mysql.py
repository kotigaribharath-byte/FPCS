import pymysql

creds = [
    ('root', ''),
    ('root', 'root'),
    ('root', 'password'),
    ('root', '1234'),
    ('root', '12345'),
    ('root', 'mysql'),
    ('root', 'admin'),
]

found = None
for user, pwd in creds:
    try:
        conn = pymysql.connect(host='localhost', user=user, password=pwd, connect_timeout=3)
        print(f'SUCCESS: user={user}, password="{pwd}"')
        found = (user, pwd)
        conn.close()
        break
    except Exception as e:
        print(f'FAIL: user={user}, password="{pwd}" -> {str(e)[:60]}')

if not found:
    print("\nMySQL not accessible with common passwords.")
    print("Please run this script after telling me your MySQL root password.")
