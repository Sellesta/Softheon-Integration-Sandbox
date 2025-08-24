import sqlite3

# 1. Connect to the database
conn = sqlite3.connect("softheon_staging.db")
cursor = conn.cursor()

# 2. Check tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables in database:", tables)

# 3. If the users table exists, fetch its data
if ('users',) in tables:
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    print("Users in table:")
    for row in rows:
        print(row)
else:
    print("No 'users' table found!")

conn.close()
