carrinho_usuario = []
soma = 0
def somar_carrinho(carrinho, somar_valores):
    for item in carrinho:
        somar_valores += item 
    if total_compras >= 500.00:
        multiplicacao = total_compras * 0.10
        subtracao = total_compras - multiplicacao
        print(f"Valor do desconto é: {multiplicacao}")
        print(f"Valor com o desconto é: {subtracao}")
    else: 
        print(f"Valor original da compra {total_compras} reias. não possui desconto!")

total_compras = int(input("Digite o valor total da compra: "))

somar_carrinho(carrinho_usuario,soma)
    