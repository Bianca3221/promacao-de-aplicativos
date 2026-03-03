idade = int(input("sua idade:" ))
ingresso = input ("tem ingresso?:" )
lista = input ("seu nome esta na lista?:" )

if idade >= 18 and (ingresso == "S" or lista == "S") :
    print ("acesso liberado")
else :
    print("acesso negado")
    

 