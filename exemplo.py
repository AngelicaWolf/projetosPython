def calcular_cedulas_moedas(valor):
    cedulas = [200, 100, 50, 20, 10, 5, 2]
    moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]
    
    resultado = {}
    
    # Calcular cédulas
    for cedula in cedulas:
        if valor >= cedula:
            quantidade = valor // cedula
            valor -= quantidade * cedula
            resultado[f"Cédula de R${cedula}"] = int(quantidade)
    
    # Calcular moedas
    for moeda in moedas:
        if valor >= moeda:
            quantidade = valor // moeda
            valor -= quantidade * moeda
            resultado[f"Moeda de R${moeda:.2f}"] = int(quantidade)
    
    return resultado

# Exemplo de uso
valor = float(input("Digite a quantia em reais: "))
resultado = calcular_cedulas_moedas(valor)

print("Para compor a quantia de R${:.2f}, você precisa de:".format(valor))
for item, quantidade in resultado.items():
    print(f"{quantidade} x {item}")
