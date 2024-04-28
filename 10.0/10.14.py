from pymongo import MongoClient
from bson.objectid import ObjectId
def atualizar_preco(produto_id, novo_preco):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['loja']
    produtos_collection = db['produtos']
    obj_id = ObjectId(produto_id)

    produtos_collection.update_one({"_id": obj_id}, {"$set": {"preco": novo_preco}})

    client.close()

    print("Preço atualizado com sucesso.")

produto_id = "000000001"  
novo_preco = 456.70
atualizar_preco(produto_id, novo_preco)
