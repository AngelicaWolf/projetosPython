stock = {
    "tomato": [50, 2.5],  
    "potato": [30, 1.8], 
    "lettuce": [20, 1.2],  
}
sale = []
def print_stock():
    print("Estoque:\n")
    for key, data in stock.items():
        print("Descrição:", key)
        print("Quantidade:", data[0])
        print("Preço: %.2f\n" % data[1])
def make_sale():
    total = 0
    print("\nVendas:\n")
    product_sold = input("Digite o nome do produto vendido: ").lower()
    if product_sold not in stock:
        print("Produto inválido! O produto não existe no estoque.")
        return
    try:
        quantity_sold = int(input(f"Quantos {product_sold} foram vendidos? "))
    except ValueError:
        print("Quantidade inválida! Por favor, digite um número inteiro.")
        return
    if quantity_sold > stock[product_sold][0]:
        print(f"Estoque insuficiente para {product_sold}. Apenas {stock[product_sold][0]} unidades disponíveis.")
        return
    price = stock[product_sold][1]
    cost = price * quantity_sold
    print(f"{product_sold.capitalize():12s}: {quantity_sold:3d} x {price:6.2f} = {cost:6.2f}")
    stock[product_sold][0] -= quantity_sold
    total += cost
    print(f"Custo total: {total:21.2f}\n")
while True:
 
    make_sale()
    continue = input("Deseja realizar outra venda? (s/n): ").lower()
    if continue != 's':
        break
print_stock()