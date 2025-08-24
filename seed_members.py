import sqlite3

DB_PATH = "softheon_staging.db"

def seed_members():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Check if table exists
    cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='members'"
    )
    if cursor.fetchone() is None:
        print("members table does not exist!")
        conn.close()
        return

    # Check if it's already seeded
    cursor.execute("SELECT COUNT(*) FROM members")
    count = cursor.fetchone()[0]
    if count > 0:
        print("members table already has data.")
        conn.close()
        return

    # Insert seed data
    cursor.execute(
        """
        INSERT INTO members (name, email)
        VALUES ('Test Member', 'member@example.com')
        """
    )
    conn.commit()
    conn.close()
    print("members table seeded with 1 test record.")

if __name__ == "__main__":
    seed_members()
