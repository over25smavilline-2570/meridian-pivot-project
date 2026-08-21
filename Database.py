import sqlite3

def init_db():
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS inventory (
            sku TEXT,
            size TEXT,
            quantity INTEGER,
            restock_date TEXT,
            PRIMARY KEY (sku, size)
        )
    """)
    # Seed initial data matching orders.js
    cursor.executemany("""
        INSERT OR REPLACE INTO inventory (sku, size, quantity, restock_date)
        VALUES (?, ?, ?, ?)
    """, [
        ("Trail Runner Jacket", "S", 14, None),
        ("Trail Runner Jacket", "M", 6, None),
        ("Trail Runner Jacket", "L", 0, "2026-08-29"),
        ("Running Shoes", "10", 0, "2026-08-24")
    ])
    conn.commit()
    conn.close()
    print("inventory.db initialized successfully!")

if __name__ == "__main__":
    init_db()
