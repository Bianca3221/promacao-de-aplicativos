nome = input(" digite seu nome")
codigo_secreto = int(input("digite seu codigo secreto: "))

if nome == "admin" and codigo_secreto == "999":
    print("acesso liberaso, sistema online")
elif nome != "admin" and codigo_secreto != "999": 
    print("acesso negado")
