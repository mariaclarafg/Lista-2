import sqlite3

def report_average_price():
    conn = sqlite3.connect('store.db')
    curser = conn.cursor()

    curser.execute('SELECT ROUND(AVG(price), 2) FROM produtos')
    average_price = curser.fetchone()[0]

    conn.close()

    return average_price

average_price = report_average_price()
print(f"Product's average price: R${average_price}")
