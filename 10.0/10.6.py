import sqlite3

def list_products():
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()

    cursor.execute('SELECT id, name, price FROM products ORDER BY name')
    products = cursor.fetchall()
    conn.close()

    return products

products = list_products()
if products:
    for product in products:
        print(product)
else:
    print("There's not products on the list")
