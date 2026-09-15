def busca_binaria(vetor, numero):
    inicio = 0
    fim = len(vetor) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if vetor[meio] == numero:
            return meio

        if numero < vetor[meio]:
            fim = meio - 1
        else:
            inicio = meio + 1

    return -1


vetor = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

numero = int(input("Digite o número que deseja encontrar: "))

indice = busca_binaria(vetor, numero)

if indice != -1:
    print("Número encontrado no índice:", indice)
else:
    print("Número não encontrado.")
