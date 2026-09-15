def busca_sequencial(lista, valor):
    contador = 0

    for elemento in lista:
        if elemento == valor:
            contador += 1

    return contador


lista = [2, 5, 7, 2, 9, 2, 4, 7, 2, 1]

valor = int(input("Digite o valor que deseja procurar: "))

quantidade = busca_sequencial(lista, valor)

print("O valor aparece", quantidade, "vezes na lista.")
