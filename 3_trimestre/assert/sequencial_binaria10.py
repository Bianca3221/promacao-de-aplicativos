def sequencial(v, x):
    c = 0
    for i in range(len(v)):
        c += 1
        if v[i] == x:
            return i, c
    return -1, c


def binaria(v, x):
    inicio = 0
    fim = len(v) - 1
    c = 0

    while inicio <= fim:
        meio = (inicio + fim) // 2
        c += 1

        if v[meio] == x:
            return meio, c
        elif x < v[meio]:
            fim = meio - 1
        else:
            inicio = meio + 1

    return -1, c


v = list(range(1, 101))

for x in [10, 50, 100]:
    print("Valor:", x)
    print("Sequencial:", sequencial(v, x))
    print("Binária:", binaria(v, x))
