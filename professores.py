import sqlite3

def criar_tabela():
    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()

    cursor.execute('''
                CREATE TABLE if NOT EXISTS professores(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    telefone TEXT,
                    materia  TEXT,
                    idade  INTEGER,
                    cpf  TEXT UNIQUE,
                    salario  REAL,
                    endereco TEXT,
                    nome_escola  TEXT ) ''')
    
    #informações para por na tabela
    nome_professor = input("Digite o nome do professor: ")
    telefone_professor = input("Digite o telefone do professor: ")
    materia_professor = input("Digite a matéria do professor: ")
    idade_professor = int(input("Digite a idade do professor: "))
    cpf_professor = input("Digite o CPF do professor: ")
    salario_professor = input("Digite o salário do professor: ")
    endereco_professor = input("Digite o endreço do professor: ")
    escola_professor = input("Digite o nome da escola: ")

    comando_inserir = (f'''
        INSERT INTO professores (nome,telefone,materia,idade,cpf,salario,endereco,nome_escola)
        VALUES ('{nome_professor}','{telefone_professor}','{materia_professor}',{idade_professor},'{cpf_professor}',
                {salario_professor},'{endereco_professor}','{escola_professor}')''')

    cursor.execute(comando_inserir)
    conexao.commit()
    conexao.close()
    
def listar_professores():
    conexao = sqlite3.connect("escola_demonstracao.db")
    cursor = conexao.cursor ()
    cursor.execute('''SELECT * FROM professores''')
    todos_professores = cursor.fetchall ()
    if not todos_professores:
        print("Nenhum professor cadastrado!")
    else:
        for professor in todos_professores:
            print(f"id = {professor[0]}, Nome = {professor[1]}, Telefone = {professor[2]}, Materia = {professor[3]}, Idade = {professor[4]},CPF = {professor[5]}, Salario = {professor[6]}, Endereço = {professor[7]},Escola = {professor[8]}")
     
    conexao.close()

def alterar_professores():
    conexao = sqlite3.connect("escola_demonstracao.db")
    cursor = conexao.cursor ()
    id_acesso = int(input("Digite o ID: "))

    cursor.execute (f"SELECT * FROM professores WHERE id = {id_acesso}")

    professores = cursor.fetchone()

    if not professores:
        print("Professor não encontrado!")
        conexao.close()
        return

    else:
        novo_nome = input("Digite o nome: ")
        novo_telefone = input("Digite o telefone : ")
        novo_endereco = input("Digite o novo endereço: ")

        comando = (f''' UPDATE professores SET nome=  '{novo_nome}',telefone= '{novo_telefone}', Endereco = '{novo_endereco}'
                    WHERE id = {id_acesso}''')
        cursor.execute(comando)
        conexao.commit()
        print("Dados alterados com sucesso!")
        conexao.close()


def excluir_professores ():
    conexao = sqlite3.connect("escola_demonstracao.db")
    cursor = conexao.cursor() 

    listar_professores()

    id_remover = int(input("Digite o ID: "))

    cursor.execute(f''' DELETE FROM professores WHERE id = {id_remover}''')

    conexao.commit()

    print("Professor removido com sucesso!") 
    conexao.close()


def menu():
    while True:
        print(" SISTEMA DE PROFESSORES! ")
        print("1. Cadastrar Professores!")
        print("2. Listar Professores!") 
        print("3. Atualizar Professores!")  
        print("4. Excluir Professores!") 
        print("5. Sair") 

        opcao = input("Escolha uma opção: ")

        if opcao == '1': criar_tabela()  
        elif opcao == '2': listar_professores()
        elif opcao == '3': alterar_professores()  
        elif opcao == '4': excluir_professores()
        elif opcao == '5': break 
        else: print("Opção inválida!")
        

menu()