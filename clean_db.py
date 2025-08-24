import pytest
import sqlite3
import os

DB_PATH = "softheon_staging.db"

@pytest.fixture(scope="function", autouse=True)
def clean_db():
    # Ensure database exists
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Clean table before each test
    cursor.execute("DELETE FROM users;")
    conn.commit()
    yield  # test runs here
    # Optionally clean after test too
    cursor.execute("DELETE FROM users;")
    conn.commit()
    conn.close()
