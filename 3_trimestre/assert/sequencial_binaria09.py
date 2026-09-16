def posicao_insercao(vetor, numero):
    inicio = 0
    fim = len(vetor)

    while inicio < fim:
        meio = (inicio + fim) // 2

        if vetor[meio] < numero:
            inicio = meio + 1
        else:
            fim = meio

    return inicio


vetor = [2, 5, 8, 12, 15, 20, 25]

numero = int(input("\nExercício 9 - Digite um número para inserir: "))

posicao = posicao_insercao(vetor, numero)

print("O número deve ser inserido na posição:", posicao)

vetor.insert(posicao, numero)

print("Vetor após a inserção:", vetor)

