def analisar_vendas(nome,lista_de_vendas,meta_mensal):
    soma = 0

    for venda in lista_de_vendas:
        soma += venda

    media = soma / len(lista_de_vendas)

    if media >= meta_mensal:
        status = print("BATEU!")

    else:
       status = print("Não bateu!")

    print(f"O vendedor {nome}, teve media de {media}, e {status} a meta ")

lista_de_vendas= [1200,1500,1100,1900]
meta = 1400
nome = "Carlos"

analisar_vendas(nome,lista_de_vendas,meta)
