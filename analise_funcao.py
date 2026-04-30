vendas = []
def analisar_vendas(nome,lista_vendas,meta_mensal):
    media_vendas = 0
    for item in lista_vendas :
        media_vendas += item 
        media_vendas /= len(lista_vendas)
    if media_vendas >= meta_mensal:
        print(f"O vendedor {nome}, com media {media_vendas} e bateu a meta!")
    else:
        print(f"O vendedor {nome}, com media {media_vendas} e não bateu a mate!")
    nome_vendedor = input("Digite o nome do vendedor: ")
    meta_mes = float(input("Qual a meta dos mes?: "))
    mais = "sim"
    while mais == "sim":
        vendas_mes = float(input("qual o vaor das vendas no mes: "))
        vendas.append(vendas_mes)
        mais = input("Tem mais valores?: ")
    analisar_vendas(nome_vendedor,vendas,meta_mes)