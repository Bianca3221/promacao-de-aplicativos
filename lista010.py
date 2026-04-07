input ("1:adicionar")
input ("2:listar")
input ("3:sair")

lista = []
opçoes = input("digite um numero de 1 a 3: ")

if opçoes == "1":
    item = input("Digite o item que deseja adicionar: ")
    lista.appen(item)
    print(lista)

elif opçoes == "2":
    item = input("digite um item para listar: ")
    print(lista)
