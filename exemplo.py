import numpy as np
def eh_identity(matrix):
    identity = np.eye(matrix.shape[0], dtype=int)  
    return np.array_equal(matrix, identity)
def ler_matrix(n):
    matrix = []
    for i in range(n):
        linha = []
        for j in range(n):
            valor = int(input(f"Digite o valor para a posição [{i}][{j}] da matriz: "))
            linha.append(valor)
        matriz.append(linha)
    return np.array(matrix)
try:
    n = int(input("Digite o tamanho da matriz quadrada (ex: 3 para 3x3): "))
    if n <= 0:
        raise ValueError("O tamanho da matriz deve ser positivo.")
    print("\nDigite os valores da matriz A:")
    A = ler_matrix(n)
    print("\nDigite os valores da matriz B:")
    B = ler_matrix(n)
    AB = np.dot(A, B)
    if eh_identity(AB):
        print("\nAs matrizes A e B são inversas, pois A * B é a matriz identidade.")
    else:
        print("\nAs matrizes A e B não são inversas, pois A * B não é a matriz identidade.")
except ValueError as e:
    print(f"Erro de valor: {e}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
