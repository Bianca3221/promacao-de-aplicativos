comprimento = input("cumprimento da peça está entre 10cm a 12cm?: ")

if comprimento == "sim":
    lagura = input("Largura da peça esta entre 5cm a 6cm?: ")
    if lagura == "sim" : 
        print("peça aprovada!")
    else:
            print("reprovado! problema na largura")
else:
    print("reprovado! peça invalida.")
    

