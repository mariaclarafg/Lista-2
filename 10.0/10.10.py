import sqlite3

def associate_product_category(product_id, category_id):
    conn = sqlite3.connect('loja.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS product_category (
                    product_id INTEGER,
                    category_id INTEGER,
                    PRIMARY KEY (product_id, category_id),
                    FOREIGN KEY (product_id) REFERENCES produtos(id),
                    FOREIGN KEY (category_id) REFERENCES categorys(id)
                )''')

    try:
        cursor.execute('INSERT INTO product_category (product_id, category_id) VALUES (?, ?)', (product_id, category_id))
    except sqlite3.IntegrityError:
        print("Association already exists in the product_category table.")
    else:
        conn.commit()
        print("Association inserted successfully.")
    conn.close()


product_id = 1
category_id = 1
associate_product_category(product_id, category_id)
