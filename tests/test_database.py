import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "softheon_staging.db"

def test_members_table_exists():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='members'")
    result = cursor.fetchone()
    conn.close()
    assert result is not None, "Members table does not exist!"

def test_members_have_data():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM members")
    count = cursor.fetchone()[0]
    conn.close()
    assert count > 0, "Members table is empty!"
