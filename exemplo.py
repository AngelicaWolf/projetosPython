estoque = {
    "tomate": [50, 2.5],  
    "batata": [30, 1.8], 
    "alface": [20, 1.2],  
}
venda = []
def imprimir_estoque():
    print("Estoque:\n")
    for chave, dados in estoque.items():
        print("Descrição:", chave)
        print("Quantidade:", dados[0])
        print("Preço: %.2f\n" % dados[1])
def realizar_venda():
    total = 0
    print("\nVendas:\n")
    produto_vendido = input("Digite o nome do produto vendido: ").lower()
    if produto_vendido not in estoque:
        print("Produto inválido! O produto não existe no estoque.")
        return
    try:
        quantidade_vendida = int(input(f"Quantos {produto_vendido} foram vendidos? "))
    except ValueError:
        print("Quantidade inválida! Por favor, digite um número inteiro.")
        return
    if quantidade_vendida > estoque[produto_vendido][0]:
        print(f"Estoque insuficiente para {produto_vendido}. Apenas {estoque[produto_vendido][0]} unidades disponíveis.")
        return
    preço = estoque[produto_vendido][1]
    custo = preço * quantidade_vendida
    print(f"{produto_vendido.capitalize():12s}: {quantidade_vendida:3d} x {preço:6.2f} = {custo:6.2f}")
    estoque[produto_vendido][0] -= quantidade_vendida
    total += custo
    print(f"Custo total: {total:21.2f}\n")
while True:
    # Realizar uma venda
    realizar_venda()
    continuar = input("Deseja realizar outra venda? (s/n): ").lower()
    if continuar != 's':
        break
imprimir_estoque()

