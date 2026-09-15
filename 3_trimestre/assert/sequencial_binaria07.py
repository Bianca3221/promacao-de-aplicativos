def busca_binaria(palavras, palavra):
    inicio = 0
    fim = len(palavras) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if palavras[meio] == palavra:
            return True

        if palavra < palavras[meio]:
            fim = meio - 1
        else:
            inicio = meio + 1

    return False


palavras = ["Ana", "Bruno", "Carlos", "João", "Maria", "Pedro"]

palavra = input("Digite o nome que deseja procurar: ")

if busca_binaria(palavras, palavra):
    print("Palavra encontrada!")
else:
    print("Palavra não encontrada.")
