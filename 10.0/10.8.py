import sqlite3

def calculate_average_price():
    conn = sqlite3.connect('loja.db')
    cursor = conn.cursor()

    cursor.execute('SELECT ROUND(AVG(price), 2) FROM products')
    average_price = cursor.fetchone()[0]

    conn.close()

    return average_price

def products_above_average():

    average_price = calculate_average_price()

    conn = sqlite3.connect('loja.db')
    cursor = conn.cursor()

    cursor.execute('SELECT name FROM products WHERE price > ?', (average_price,))
    products_above_average = cursor.fetchall()
    conn.close()

    product_names_above_average = [product[0] for product in products_above_average]

    return product_names_above_average

products_above_avg = products_above_average()
if products_above_avg:
    print("Products with price above average:")
    for product in products_above_avg:
        print(product)
else:
    print("No products with price above average.")
