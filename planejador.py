open('planejamento.viagem', 'w').close()

def criar_destino():
    destino = input("Coloque o destino desejado:")
    with open('planejamento.viagem', 'a') as f:
        f.write(destino + '\n')
        print("Destino adicionado! ")

def ler():
    with open('planejamento.viagem', 'r') as f:
        lugares = f.readlines()

        i=0
        for lugar in lugares:
            print(f"{i} - {lugar.strip()}")
            i +=1 


def atualizar():
    ler()
    indice = int(input("Digite o ID do lugar que deseja alterar: "))
    novo_destino = input("Destino novo :")

    with open('planejamento.viagem', 'r') as f :
        linhas = f.readlines()

    linhas[indice] = novo_destino + '\n'

    with open('planejamento.viagem', 'w') as f:
        f.writelines(linhas)
    print("Destino atualizado")



def remover():
    ler()
    indice = int(input("Digite o ID do lugar que deseja excluir: "))

    with open('planejamento.viagem', 'r') as f :
       linhas = f.readlines()
    
    del linhas[indice]
    with open('planejamento.viagem', 'w') as f : 
        f.writelines(linhas)

    print("Aluno removido!")


while True :
    print("\n1-Cadastrar,| 2-Listar | 3-Editar | 4- Excluir | 5-Sair")
    opcao = input("Escolha:")
        
    if opcao == '1' : criar_destino()
    elif opcao == '2': ler()
    elif opcao == '3': atualizar()
    elif opcao == '4' : remover()
    elif opcao == '5' : break

