open('bons.habitos','w').close()

def novo_habito():
    habitos = input("Coloque um habito: ")
    with open('bons.habitos' , 'a') as f :
        f.write( habitos + '/n')
        print("Habito adicionado!")

def revisar_habitos():
    with open('bons.habitos' , 'r') as f:
        habitos = f.readlines()

        h = 0
        for habito in habitos :
            print(f"{h} - {habito.strip()} ")
            h += 1

        
def habitos_atualizados():
    revisar_habitos()
    indice = input("Digite o ID do habito que deseja alterar: ")
    novo_habito = input("Digite um novo habito: ")

    with open('bons.habito', 'r') as f :
        linhas = f.writelines()

    linhas[indice] = novo_habito + '\n'

    with open('bons.habitos', 'w')as f :
        f.writelines(linhas)
    print("Hábito atualizado!")
    

