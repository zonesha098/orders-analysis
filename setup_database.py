import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("orders.db")
cursor = conn.cursor()

# Create customers table
cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    city TEXT NOT NULL
)
""")

# Create orders table
cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    amount REAL NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
)
""")

# Insert 6 customers
customers = [
    (1, "Ali", "Islamabad"),
    (2, "Sara", "Lahore"),
    (3, "Ahmed", "Karachi"),
    (4, "Ayesha", "Islamabad"),
    (5, "Usman", "Lahore"),
    (6, "Hina", "Karachi")
]

cursor.executemany("""
INSERT OR IGNORE INTO customers
(customer_id, name, city)
VALUES (?, ?, ?)
""", customers)

# Insert 10 orders
orders = [
    (1, 1, 8000),
    (2, 1, 4500),
    (3, 2, 7000),
    (4, 2, 3000),
    (5, 3, 9000),
    (6, 4, 6000),
    (7, 4, 7500),
    (8, 5, 4000),
    (9, 6, 6500),
    (10, 6, 5500)
]

cursor.executemany("""
INSERT OR IGNORE INTO orders
(order_id, customer_id, amount)
VALUES (?, ?, ?)
""", orders)

conn.commit()
conn.close()

print("Database created successfully.")
print("6 customers and 10 orders inserted.")