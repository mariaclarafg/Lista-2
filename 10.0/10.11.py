client = MongoClient('mongodb://localhost:27017/')

db = client['store']

products_collection = db['products']

if 'products' in db.list_collection_names():
    print("Collection 'products' created successfully.")
else:
    print("Failed to create collection 'products'.")

client.close()
