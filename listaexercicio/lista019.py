valor_da_compra = float(input("Digite o valor da compra: "))
cupom = input("Tem cupom?: ")

if valor_da_compra >= 100 and cupom == "sim" :
    multiplicacao = valor_da_compra  * 0.10
    valor_com_desconto = valor_da_compra - multiplicacao
    print(f"Sua compra foi {valor_com_desconto} reais. ")

else:
    print("Você não tem desconto!")