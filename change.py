def change():
    expense = 23.75
    money = 100
    vuelto = money - expense #76,25
    vuelto_pesos = int(vuelto) # 76
    centavos = int((vuelto - vuelto_pesos)*100) # 76,25 - 76  = 0,25 * 100 = 25
    print("Ingresar gasto")
    print(expense)
    print("Dinero recibido")
    print(money)
    print("")
    print("Vuelto")
    print("")
    print("Pesos:")
    print(vuelto_pesos)
    print("Centavos:")
    print(centavos) 
