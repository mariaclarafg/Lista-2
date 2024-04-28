try:
    arquivo = open("arquivo.txt", "r")
    conteudo = arquivo.read()
except FileNotFoundError as erro:
    raise ValueError("Erro ao ler arquivo") from erro
except Exception as e:
    print(f"Erro genérico: {e}")
