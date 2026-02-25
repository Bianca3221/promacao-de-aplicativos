valor_da_compra = float(input("digite o valor da compra: "))
cupom = input("digite seu cupom: ")


if cupom == "DEV10" :
    multiplicacao = compra * 0.10
    valor_com_desconto = multiplicacao - compra
    print("valor com desconto: ", valor_com_desconto)
else:
    print("cupom inválido. Valor original: R$ [valor]")
