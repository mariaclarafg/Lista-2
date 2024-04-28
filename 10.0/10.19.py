from pymongo import MongoClient

def inserir_categoria(categoria_id, categoria_nome):
    client = MongoClient('mongodb://localhost:00000/')
    db = client['loja']
    categorias_collection = db['categorias']

    if 'categorias' not in db.list_collection_names():
        db.create_collection('categorias')

    categorias_collection.insert_one({"_id": categoria_id, "nome": categoria_nome})
    client.close()

    print("Categoria criada com sucesso.")

categoria_id = 1 
categoria_nome = "Livros"
inserir_categoria(categoria_id, categoria_nome)
