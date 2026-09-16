def maior_numero(vetor):
    maior = vetor[0]
    posicao = 0

    for numero in vetor:
        if numero > maior:
            maior = numero
            posicao = vetor.index(numero)

    return maior, posicao


vetor = [3, 8, 2, 15, 7, 10, 4, 6, 12, 5]

maior, posicao = maior_numero(vetor)

print("Maior número:", maior)
print("Posição:", posicao)
