nomes = ["Julia","Maria","gabi","Enzo"]

antigo= input("qual o nome você quer mudar?: ")
novo = input("qual o nome? ")

for i in range(len(nomes)):
    if nomes[antigo] == antigo:
        nomes[novo] = novo

print("lista atualizada:", nomes)