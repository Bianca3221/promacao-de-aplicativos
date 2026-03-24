autorizados = ["Alice","Bob","Carlos"]
nome = input("Digite o nome de um pesquisador: ")
if nome in autorizados:
    print(f"Acesso permitido! O pesquisador {nome} esta na posição", autorizados.index(nome))
    pergunta = input("Deseja remover esse pequisador da lista? (Sim/Não): ");



    if pergunta == "Sim":
        autorizados.remove(nome)
        print(f"Agora os membros da lista são {autorizados}")
    else:
        print("Encerrando programa...")

else:
    print(f"Agora os membros da lista são {nome} não foi encontrado")
    pergunta2 = input ("deseja cadastrar esse nome como novo pesquisador? (Sim/Não): ")
    if pergunta2 == "Sim":
        autorizados.append(nome) 
        print(f"lista atualizada {autorizados}")
        
