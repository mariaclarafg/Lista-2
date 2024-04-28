from pymongo import MongoClient

client = MongoClient('mongodb://localhost:0000/')

db = client['store']
products_collection = db['products']

products_collection.insert_one({"name": "Book", "price": 9.99})
products_collection.insert_one({"name": "Tabletr", "price": 149.99})
products_collection.insert_one({"name": "PC", "price": 499.99})

print("Document insertion successful.")
client.close()
