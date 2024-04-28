from pymongo import MongoClient

def listar_produtos():
    client = MongoClient('mongodb://localhost:27017/')

    db = client['loja']
    produtos_collection = db['produtos']

    produtos = produtos_collection.find().sort("nome", 1)

    produtos_list = []

    for produto in produtos:
        produtos_list.append({
            "_id": str(produto["_id"]),
            "nome": produto["nome"],
            "preco": produto["preco"]
        })

    client.close()

    return produtos_list

produtos = listar_produtos()
for produto in produtos:
    print(produto)
