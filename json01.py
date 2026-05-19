import json 

frase = input("Digite sua frase aqui: ")

dados = {"mensagem": frase }

with open("teste.json", "w", encoding= "utf-8") as arquivos :
    json.dump(dados, arquivos, ensure_ascii=False,indent=4)

print(" Arquivo teste.json criado com sucesso!")