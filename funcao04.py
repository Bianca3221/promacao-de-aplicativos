minha_lista_fruta = ["maçã","banana","uva","pera","abacaxi"]
minha_lista_ferramenta = ["martelo","prego","chave"]

def esta_na_lista (nome, lista):
    if nome in lista:
        print("Encontrado")
    else:
        print("Não disponivel")
    nome = input ("Digite o nome: ")
    lista = input ("Digite a lista: ")
    if lista == "frutas":
        lista = minha_lista_fruta
    elif lista == "ferramentas":
        lista = minha_lista_ferramenta
    esta_na_lista(nome, lista)

