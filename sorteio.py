seu_id = int(input("digite seu id: "))
valor_da_compra = float(input("Digite o valor da compra: "))

if seu_id % 2 == 0 and valor_da_compra >= 500 :
    print(f"Parabéns usuário {seu_id} ! você ganhou um cupom para a sua compra de R$ {valor_da_compra} ")

else:
    print(f"Obrigado pela compra, usuário {seu_id}. Continue acompanhando nossas promoções :) ")
