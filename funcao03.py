nova_lista = []
def aplicar_promocao(precos):

    for preco in precos:
        if preco > 100.00:
            preco_novo = preco * 0.15
            nova_lista.append(preco_novo)

        else:
            nova_lista.append(preco)

    return nova_lista
valor_compra = float(input("Digite o valor da compra: "))
compras = [150.0,80.0,200.0,50.0]

precos_atualizados = aplicar_promocao (compras)