media = float(input("digite sua média: "))
renda = float(input("sua renda é: "))
escola = input(" escola publica ou privada: ")

if media >= 8.0 and (renda <= 2000.00 or escola == "publica" ):
    print("Ganhou a bolsa ")
else:
    print("Voce não atende aos requisitos")
    

