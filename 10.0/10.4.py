import sqlite3

def update_product(product_id, new_price):
    conn = sqlite3.connect('loja.db')
    cursor = conn.cursor()

    cursor.execute('UPDATE products SET price = ? WHERE id = ?', (new_price, product_id))

    conn.commit()

    conn.close()

    print("Price sucessfully updated.")

product_id = 1
new_preco = 30.99
update_product(product_id, new_preco)
