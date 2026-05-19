open('bonshabitos.txt','w').close()

def novo_habito():
    habitos = input("Coloque um habito: ")
    with open('bonshabitos.txt' , 'a') as f :
        f.write( habitos + '/n')
        print("Habito adicionado!")

def revisar_habitos():
    with open('bonshabitos.txt' , 'r') as f:
        habitos = f.readlines()

        h = 0
        for habito in habitos :
            print(f"{h} - {habito.strip()} ")
            h += 1

        
def habitos_atualizados():
    revisar_habitos()
    indice = int(input("Digite o ID do habito que deseja alterar: "))
    novo_habito = input("Digite um novo habito: ")

    with open('bonshabito.txt', 'r') as f :
        linhas = f.writelines()

    linhas[indice] = novo_habito + '\n'

    with open('bonshabitos.txt', 'w')as f :
        f.writelines(linhas)
    print("Hábito atualizado!")

def remover():
    revisar_habitos()
    indice = int(input("Digite o ID do hábito que deseja remover: "))

    with open('bonshabitos.txt', 'r') as f:
        linhas = f.readlines()

    del linhas[indice]
    with open('bonshabitos.txt', 'w') as f: 
        f.writelines(linhas)

    print("Hábito removido!")

    
while True :
    print("\n1-Cadastrar,| 2-Listar | 3-Editar | 4- Excluir | 5-Sair")
    opcao = input("Escolha:")
        
    if opcao == '1' : novo_habito()
    elif opcao == '2': revisar_habitos()
    elif opcao == '3': habitos_atualizados()
    elif opcao == '4' : remover()
    elif opcao == '5' : break