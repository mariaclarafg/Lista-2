from pymongo import MongoClient
from bson.objectid import ObjectId

def search_product(product_id):
    client = MongoClient('mongodb://localhost:7/')


    db = client['loja']
    products_collection = db['products']

    obj_id = ObjectId(product_id)
    product = products_collection.find_one({"_id": obj_id})

    client.close()


    if product:
        return {"name": product["name"], "price": product["price"]}
    else:
        return None

product_id = "a1b2c3d4"
found_product = search_product(product_id)
if found_product:
    print("Found product:")
    print(found_product)
else:
    print("Product not found.")
