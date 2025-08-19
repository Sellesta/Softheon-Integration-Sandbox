import sqlite3

def fetch_members(db_path: str, sql_file: str):
    """Fetch members using a local SQLite database for testing."""
    with open(sql_file, 'r') as f:
        query = f.read()
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
    return rows

if __name__ == "__main__":
    # Example: using a test SQLite DB (in real life, this could be Postgres/SQL Server)
    db_path = "../mock_softheon.db"  # Assume a local SQLite DB for simulation
    sql_file = "fetch_members.sql"
    try:
        members = fetch_members(db_path, sql_file)
        print(f"Fetched {len(members)} members:")
        for row in members[:5]:
            print(row)
    except Exception as e:
        print("Integration test failed:", e)
