import sqlite3
import random

class ElectronicsDB:
    def __init__(self, db_name="electronics.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                price REAL
            )
        """)
        self.conn.commit()

    def insert_product(self, name, price):
        self.cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", (name, price))
        self.conn.commit()

    def update_product(self, product_id, name=None, price=None):
        query = "UPDATE products SET "
        params = []
        if name:
            query += "name = ?, "
            params.append(name)
        if price:
            query += "price = ?, "
            params.append(price)
        query = query.rstrip(", ") + " WHERE id = ?"
        params.append(product_id)
        self.cursor.execute(query, tuple(params))
        self.conn.commit()

    def delete_product(self, product_id):
        self.cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
        self.conn.commit()

    def select_product(self, product_id):
        self.cursor.execute("SELECT * FROM products WHERE id = ?", (product_id,))
        return self.cursor.fetchone()

    def list_products(self):
        self.cursor.execute("SELECT * FROM products")
        return self.cursor.fetchall()

    def __del__(self):
        self.conn.close()

# Example Usage
db = ElectronicsDB()

# List of sample product names
product_names = ["Smartphone", "Laptop", "Tablet", "Headphones", "Smartwatch", "Camera", "Printer"]

# Inserting sample data
for _ in range(100):
    name = random.choice(product_names)
    price = round(random.uniform(100, 2000), 2)
    db.insert_product(name, price)

# Displaying all products
products = db.list_products()
for product in products:
    print(product)

# Updating a product
db.update_product(1, name="New Smartwatch", price=299.99)

# Deleting a product
db.delete_product(1)

# Fetching a product
product = db.select_product(2)
print(product)
