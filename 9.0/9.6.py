import math

def calcular_raiz_quadrada(numero):
    try:
        raiz_quadrada = math.sqrt(numero)
        return raiz_quadrada
    except ValueError:
        print("Não é possível calcular a raiz quadrada pois o numero é negativo.")
        return None

try:
    numero = float(input("Digite um número positivo para calcular a raiz quadrada: "))
    
    if numero < 0:
        raise ValueError("O número não pode ser negativo.")
    
    resultado = calcular_raiz_quadrada(numero)
    if resultado is not None:
        print(f"A raiz quadrada de {numero} é: {resultado:.2f}")
except ValueError as v:
    print(f"Erro: {v}")