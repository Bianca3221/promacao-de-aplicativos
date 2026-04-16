nomes = ["Julia","Gabriel","Ana","Enzo"]
notas = [8.8,4.9,5.8,7.3]

for n in notas:
    if n >=6:
        indice = notas.index(n)
        print(nomes[indice])