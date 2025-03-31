def change():
    expense = 23.75
    money = 100
    print("Ingresar Gasto")
    print(expense)
    print("Dinero recibido")
    print(money)
    print()
    print("Vuelto")
    print()
    print("Pesos:")
    print(int(money - expense))
    print("Centavos:")
    centavos = (money - expense) - (int(money - expense))
    print(int(centavos * 100)) 
