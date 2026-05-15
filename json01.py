import json 

frase = input("Digite sua frase aqui: ")

dados = {"mensagem": frase }

with open("teste.json", "w", encoding= "utf-8") as arquivos :
    json.dump