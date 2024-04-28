import sqlite3

def delete_product(product_id):
    conn = sqlite3.connect('loja.db')
    cursor = conn.cursor()

    cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))

    conn.commit()
    conn.close()
    print("Product sucessfully deleted")

product_id = 1
delete_product(product_id)
