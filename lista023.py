nota01 = float(input("Digite sua nota: "))
nota02 = float(input("digite sua nota: "))
nota03 = float(input("digite sua nota: "))
nota04 = float(input("digite sua nota: "))
media = 0.0

lista = []
  
lista.append(nota01)
lista.append(nota02)
lista.append(nota03)
lista.append(nota04)

for l in lista:
    media += l 

media_final = media /4

print(f"Media: {media}")

if media_final >= 7:
    print("aprovado")
elif media_final >= 5 and media_final >6.9:
    print("Recuperação")
else:
    print("reprovado")

