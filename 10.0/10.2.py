import sqlite3

conn = sqlite3.connect('loja.db')
cursor = conn.cursor()

products_data = [
    ('Product 1', 10.99),
    ('Product 2', 15.49),
    ('PRoduct 3', 7.25)
]

cursor.executemany('INSERT INTO products (name, price) VALUES (?, ?)', products_data)

conn.commit()
conn.close()

print("Products sucessfully inserted.")
