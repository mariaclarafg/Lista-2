import sqlite3

def insert_category(category_id, category_name):
    conn = sqlite3.connect('loja.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS categorys (
                    id INTEGER PRIMARY KEY,
                    name TEXT
                )''')

    cursor.execute('INSERT INTO categorys (id, name) VALUES (?, ?)', (category_id, category_name))
    conn.commit()

    conn.close()

    print("New category sucessfully created.")

category_id = 1
category_name = "Food"
insert_category(category_id, category_name)
