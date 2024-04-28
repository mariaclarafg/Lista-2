from pymongo import MongoClient
from bson.objectid import ObjectId

def adicionar_categoria_produto(produto_id, categoria_id):
    client = MongoClient('mongodb://localhost:00000/')

    db = client['loja']
    produtos_collection = db['produtos']
    categorias_collection = db['categorias']
    obj_id = ObjectId(produto_id)
    produto_existente = produtos_collection.find_one({"_id": obj_id})

    if produto_existente:
        produtos_collection.update_one({"_id": obj_id}, {"$set": {"categoria_id": categoria_id}})
        categorias_collection.insert_one({"_id": categoria_id, "produto_id": produto_id})

        print("Categoria adicionada ao produto com sucesso.")
    else:
        print("Produto não encontrado.")
    client.close()

produto_id = "60579dc4f7028b7a1a9430e1"  # 
categoria_id =
adicionar_categoria_produto(produto_id, categoria_id)
