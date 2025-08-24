import sqlite3

def insert_user(username, email):
    conn = sqlite3.connect("softheon_staging.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, email) VALUES (?, ?)", (username, email))
    conn.commit()
    conn.close()

def fetch_users():
    conn = sqlite3.connect("softheon_staging.db")
    cursor = conn.cursor()
    cursor.execute("SELECT username, email FROM users")
    rows = cursor.fetchall()
    conn.close()
    return rows

def test_user_insert_and_read():
    insert_user("pytest_user", "pytest@example.com")
    users = fetch_users()
    assert ("pytest_user", "pytest@example.com") in users
