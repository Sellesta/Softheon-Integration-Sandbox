import sqlite3

# Adjust filename if needed
conn = sqlite3.connect("softheon_staging.db")  
cursor = conn.cursor()

cursor.execute("SELECT * FROM users;")
rows = cursor.fetchall()

if rows:
    print("Users table contents:")
    for row in rows:
        print(row)
else:
    print("No rows found in users table.")

conn.close()
