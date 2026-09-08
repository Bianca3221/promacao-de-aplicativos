import banco 
import escola 
import turmas
import aluno

def menu_escolas():
    while True:
        print("MENU:")
        print("1 - Cadastrar escola")
        print("2 - Listar escolas")
        print("3 - Alterar escola")
        print("4 - Excluir escola")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome da escola: ")
            cidade = input("Digite a cidade: ")

            escola.cadastrar_escola(nome, cidade)


        elif opcao == "2" :
            aluno.listar_alunos()


        elif opcao == "3":
            try:
                id_aluno = int(input("ID do aluno: "))
                nome = input("Novo nome: ")
                idade = int(input("Nova idade: "))
                id_turma = int(input("Novo ID da turma: "))

                aluno.alterar_aluno(
                    id_aluno,
                    nome,
                    idade,
                    id_turma
                )

            except ValueError:
                print("Digite números válidos para ID, idade e turma.")


        elif opcao == "4":
            try:
                id_aluno = int(input("ID do aluno que deseja excluir: "))

                aluno.excluir_aluno(id_aluno)

            except ValueError:
                print("Digite um número válido para o ID.")

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")


def Menu():
    banco.criar_tabelas()

    while True:
        print("GESTÃO ESCOLAR")
        print("1 - Escolas")
        print("2 - Turmas")
        print("3 - Alunos")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_escolas()

        elif opcao == "2":
            menu_turmas()

        elif opcao == "3":
            menu_alunos()

        elif opcao == "0":
            print("Sistema encerrado.")
            break

        else:
            print("Opção inválida. Tente novamente.")

Menu()







