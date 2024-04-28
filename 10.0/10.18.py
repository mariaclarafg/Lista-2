from pymongo import MongoClient

def relatorio_preco_medio():
    client = MongoClient('mongodb://localhost:00000/')

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

def produtos_acima_media():
    client = MongoClient('mongodb://localhost:000000/')
    db = client['loja']
    produtos_collection = db['produtos']
    media_preco = relatorio_preco_medio()

    if media_preco is not None:
        produtos_acima_media = list(produtos_collection.find({"preco": {"$gt": media_preco}}))
        nomes_produtos_acima_media = [produto["nome"] for produto in produtos_acima_media]
        return nomes_produtos_acima_media
    else:
        return []

nomes_produtos_acima_media = produtos_acima_media()
if nomes_produtos_acima_media:
    print("Produtos com preço acima da média: ")
    for nome in nomes_produtos_acima_media:
        print(nome)
else:
    print("Não há produtos com preço acima da média.")
