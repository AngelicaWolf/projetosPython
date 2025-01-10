def calculate_bills_coins(value):
    bills = [200, 100, 50, 20, 10, 5, 2]
    coins = [1, 0.50, 0.25, 0.10, 0.05, 0.01]
    
    result = {}
    
    for bill in bills:
        if value >= bill:
            quantity = value // bill
            value -= quantity * bill
            result[f"Cédula de R${bills}"] = int(quantity)
    
    for coin in coins:
        if value >= coin:
            quantity = value // coin
            value -= quantity * coin
            result[f"Coin de R${coin:.2f}"] = int(quantity)
    
    return result

value = float(input("Digite a quantia em reais: "))
result = calculate_bills_coins(value)

print("Para compor a quantia de R${:.2f}, você precisa de:".format(value))
for item, quantity in result.items():
    print(f"{quantity} x {item}")
