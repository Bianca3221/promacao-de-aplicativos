saldo_inicial = 500 
print("1-Depositar, 2-sacar,3-sair")
opcao = int(input("digite a opção desejada: "))
while opcao != 3:
    if opcao == 1:
        valor = float(input("digite o valor: "))
        if valor > 0.00:
            valor_final = saldo_inicial - valor 
            print(f"seu saldo é {valor_final}")

    elif opcao == 2:
        saque = float(input("Digite o valor:"))
        if saque > saldo: 
            print("saldo insuficiente")

    elif opcao == 3 :
        print("saindo do programa")

    opcao = int(input("digite a opção desejada: "))

