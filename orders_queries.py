import sqlite3

# Connect to database
conn = sqlite3.connect("orders.db")
cursor = conn.cursor()

# (a) INNER JOIN
print("\n(a) Customer names and their order amounts:")

cursor.execute("""
SELECT customers.name, orders.amount
FROM customers
INNER JOIN orders
ON customers.customer_id = orders.customer_id
""")

for row in cursor.fetchall():
    print(row)


# (b) GROUP BY + SUM()
print("\n(b) Total amount spent per customer:")

cursor.execute("""
SELECT customers.name, SUM(orders.amount) AS total_spent
FROM customers
INNER JOIN orders
ON customers.customer_id = orders.customer_id
GROUP BY customers.customer_id, customers.name
ORDER BY total_spent DESC
""")

for row in cursor.fetchall():
    print(row)
# (c) GROUP BY + HAVING
print("\n(c) Cities where average order amount exceeds Rs. 5000:")

cursor.execute("""
SELECT customers.city, AVG(orders.amount) AS average_order_amount
FROM customers
INNER JOIN orders
ON customers.customer_id = orders.customer_id
GROUP BY customers.city
HAVING AVG(orders.amount) > 5000
""")

for row in cursor.fetchall():
    print(row)
conn.close()