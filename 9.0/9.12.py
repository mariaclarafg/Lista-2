class ValorInvalido(Exception): 
    def __init__(self, parametro, valor): 
        self.parametro = parametro 
        self.valor = valor 
        self.mensagem = f"O valor '{valor}' é inválido para o parâmetro '{parametro}'" 
        super().__init__(self.mensagem)


def calcula_idade(ano_nascimento): 
    if ano_nascimento < 1900 or ano_nascimento > 2023: 
        raise ValorInvalido("ano_nascimento", ano_nascimento) 
    else: 
        return 2024 - ano_nascimento

try: 
    idade = calcula_idade(1880) 
except ValorInvalido as erro: 
    print(erro.mensagem)
