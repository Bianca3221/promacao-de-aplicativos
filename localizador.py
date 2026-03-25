cidades = ["São Paulo","Rio de Janiro","Curitiba","Belo Horizonte"]
cidade2 = input("Digite o nome o nome de uma cidade: ")
if cidade2 in cidades:
    print(f"A cidade {cidade2} está na posição", cidade2.index(cidade2))

else:
    print(f"A cidade {cidade2} não tem na lista!")
    