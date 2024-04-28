from pymongo import MongoClient

def relatorio_preco_medio():
    client = MongoClient('mongodb://localhost:0000/')
    db = client['loja']
    produtos_collection = db['produtos']

    pipeline = [{"$group": {"_id": None, "preco_medio": {"$avg": "$preco"}}}]
    resultado = list(produtos_collection.aggregate(pipeline))

    client.close()
    if resultado:
        preco_medio = round(resultado[0]['preco_medio'], 2)
        return preco_medio
    else:
        return None

preco_medio = relatorio_preco_medio()
if preco_medio is not None:
    print(f"Preço médi: R${preco_medio}")
else:
    print("Não ha dados para calcular o preço médio")
