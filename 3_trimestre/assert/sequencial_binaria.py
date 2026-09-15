def busca_sequencial(vetor, numero):
    for valor in vetor:
        if valor == numero:
            return vetor.index(valor)
    return -1


vetor = [3, 1, 9, 7, 2, 5, 8, 4, 6, 10]

numero = int(input("Digite o número que deseja encontrar: "))

indice = busca_sequencial(vetor, numero)

if indice != -1:
    print("Número encontrado no índice:", indice)
else:
    print("Número não encontrado.")

