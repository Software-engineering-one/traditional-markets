import sqlite3

conn = sqlite3.connect('inventory_database.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS inventory (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item_name TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        expiration_date TEXT NOT NULL
    )
''')

def insert_inventory(item_name, quantity, expiration_date):
    cursor.execute('''
        INSERT INTO inventory (item_name, quantity, expiration_date) VALUES (?, ?, ?)
    ''', (item_name, quantity, expiration_date))
    conn.commit()

insert_inventory("Apple", 100, "2024-12-01")
insert_inventory("Banana", 150, "2024-11-15")
insert_inventory("Orange", 200, "2025-01-10")

def fetch_all_inventory():
    cursor.execute('SELECT * FROM inventory')
    return cursor.fetchall()

inventory_items = fetch_all_inventory()
for item in inventory_items:
    print(f"ID: {item[0]}, Item Name: {item[1]}, Quantity: {item[2]}, Expiration Date: {item[3]}")

conn.close()