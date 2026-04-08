carrinho = []
produto = ""

while produto != "sair" :
    produto = input("digite o produto desejado: ")
    if produto != "sair":
        carrinho.append(produto)
    print (carrinho)