try:
    arquivo = open('dados.txt', 'w')
    arquivo.write('Dados importantes')
except Exception as e:
    print(f"Erro durante a escrita no arquivo: {e}")
finally:
    try:
        if arquivo:
            arquivo.close()
            print("Arquivo fechado com sucesso.")
    except Exception as e:
        print(f"Erro ao fechar o arquivo: {e}")