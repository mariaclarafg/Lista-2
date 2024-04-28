import sqlite3

def find_product(product_id):
    conn = sqlite3.connect('loja.db')
    cursor = conn.cursor()


    cursor.execute('SELECT name, price FROM products WHERE id = ?', (product_id,))
    product = cursor.fetchone()

    conn.close()

    if product:
        return product
    else:
        return None

product_id = 1
resultado = find_product(product_id)
if resultado:
    name, price = resultado
    print(f"Found product - Name: {name}, Price: {price}")
else:
    print("Not found product.")