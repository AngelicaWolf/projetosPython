PC= {"Lamborghini Aventador":1500000.00,"Dodge Viper": 1100000.00,"Porsche Cayenne": 200000.00,"Ford Mustang": 350000.00,"Ferrari Enzo":12000000.00}
for carro, preco in PC.items():
    print(f"{carro}: R$ {preco:,.2f}")
while True:
    carro_input = input("Digite o nome do carro ou 'fim' para sair: ")
    if carro_input.lower() == 'fim':
        break
    if carro_input in PC:
        print(f"Preço de {carro_input}: R$ {PC[carro_input]:,.2f}")
    else:
        print("Carro não encontrado. Tente novamente.")
print("\nTodos os carros e seus preços:")
for carro, preco in PC.items():
    print(f"{carro}: R$ {preco:,.2f}")
print("Porsche Cayenne" in PC) 
print("Tesla Model S" in PC)  
print("Chaves (nomes dos carros):", PC.keys())
print("Valores (preços):", PC.values())
