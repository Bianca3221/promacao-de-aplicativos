saldo_inicial = 1000.00
print ("1-deposito, 2-saque, 3-extrato")
menu_inicial = int(input("digite uma das opçoes escolhido:"))

if menu_inicial == 1:
    valor = float(input("digite o valor:"))
    if valor > 0.00:
        valor_final = saldo_inicial + valor
        print("seu saldo é:", valor_final)

elif menu_inicial == 2 :
    valor = float(input("digite o valor: "))
    if valor > 0.0 and (valor <= saldo_inicial or valor == 100):
        valor_final = saldo_inicial - valor
        print("seu saldo é:", valor_final)
    else:
        print("saldo insuficiente! ")

elif menu_inicial == 3 :
    print("seu saldo é:", saldo_inicial)

        







































