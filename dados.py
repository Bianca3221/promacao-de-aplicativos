compras = []
item = ""
while item != "fim":
    item = input("item a ser adicionado na lista: ")
    compras.append(item)
compras.remove("fim")
print(f"fim da lista de compra, a lista atual agora é: {compras}")