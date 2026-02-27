nome = input("digite seu nome: ")
valor_da_compra = float(input("digite o valor da compra: "))
distancia = int(input("digite a distancia da entrega: "))
cupom = input("digite seu cupom: ")
frete = 40.00

if valor_da_compra >= 1000.00 and cupom == "S":
    multiplicacao = valor_da_compra * 0.20
    valor_com_desconto = multiplicacao - valor_da_compra 
    print("parabéns! Você ganhou um , mouse pad gamer de brinde ")

elif valor_da_compra > 500.00 and valor_da_compra < 1000.00 and cupom == "S": 
    multiplicacao = valor_da_compra * 0.10
    valor_com_desconto = multiplicacao - valor_da_compra

elif distancia <= 50 and valor_da_compra > 200.00:
    frete = 0.00
    valor_com_desconto = valor_da_compra + frete
else:
    total = valor_com_desconto + frete 

print ("olá, ", nome)
print ("o valor da compra é", valor_da_compra )
print (" valor do desconto", cupom )
print ("valor da compra com desconto", valor_com_desconto )




