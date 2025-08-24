import sqlite3

def insert_user(username, email):
    conn = sqlite3.connect("softheon_staging.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO users (username, email, created_at)
        VALUES (?, ?, CURRENT_TIMESTAMP)
        """,
        (username, email)
    )
    conn.commit()
    conn.close()
