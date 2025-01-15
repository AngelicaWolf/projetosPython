pc= {"Lamborghini Aventador":1500000.00,"Dodge Viper": 1100000.00,"Porsche Cayenne": 200000.00,"Ford Mustang": 350000.00,"Ferrari Enzo":12000000.00}
for car, price in pc.items():
    print(f"{car}: R$ {price:,.2f}")
while True:
    car_input = input("Digite o nome do carro ou 'fim' para sair: ")
    if car_input.lower() == 'fim':
        break
    if car_input in pc:
        print(f"Preço de {car_input}: R$ {pc[car_input]:,.2f}")
    else:
        print("Carro não encontrado. Tente novamente.")
print("\nTodos os carros e seus preços:")
for car, price in pc.items():
    print(f"{car}: R$ {price:,.2f}")
print("Porsche Cayenne" in pc) 
print("Tesla Model S" in pc)  
print("Chaves (nomes dos carros):", pc.keys())
print("Valores (preços):", pc.values())
