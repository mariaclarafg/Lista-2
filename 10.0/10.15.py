from pymongo import MongoClient
from bson.objectid import ObjectId

def excluir_produto(produto_id):
    client = MongoClient('mongodb://localhost:000000/')
    db = client['loja']
    produtos_collection = db['produtos']

    obj_id = ObjectId(produto_id)


    produtos_collection.delete_one({"_id": obj_id})
    client.close()

    print("Produto excluído com sucesso.")


produto_id = "00000000000000"
excluir_produto(produto_id)
