import numpy as np
def eh_identidade(matriz):
    identidade = np.eye(matriz.shape[0], dtype=int)  
    return np.array_equal(matriz, identidade)
def ler_matriz(n):
    matriz = []
    for i in range(n):
        linha = []
        for j in range(n):
            valor = int(input(f"Digite o valor para a posição [{i}][{j}] da matriz: "))
            linha.append(valor)
        matriz.append(linha)
    return np.array(matriz)
try:
    n = int(input("Digite o tamanho da matriz quadrada (ex: 3 para 3x3): "))
    if n <= 0:
        raise ValueError("O tamanho da matriz deve ser positivo.")
    print("\nDigite os valores da matriz A:")
    A = ler_matriz(n)
    print("\nDigite os valores da matriz B:")
    B = ler_matriz(n)
    AB = np.dot(A, B)
    if eh_identidade(AB):
        print("\nAs matrizes A e B são inversas, pois A * B é a matriz identidade.")
    else:
        print("\nAs matrizes A e B não são inversas, pois A * B não é a matriz identidade.")
except ValueError as e:
    print(f"Erro de valor: {e}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
