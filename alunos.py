import sqlite3

def cadastrar_aluno() :
    # 1. CONEXÃO: Abre ou cria o arquivo do banco de dados import sqlite3
    conexao = sqlite3.connect("escola_demonstracao.db")
    cursor = conexao.cursor ()

    # 2 passo CRIAÇÃO DA TABELA 
    cursor.execute('''
                    CREATE TABLE if NOT EXISTS alunos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        telefone TEXT,
                        turma TEXT,
                        idade INTEGER,
                        cpf TEXT UNIQUE NOT NULL,
                        id_professor INTEGER,
                        FOREIGN KEY (id_professor) REFERENCES professores (id) 
                        )''')

    # 3. INFORMAÇÕES DO ALUNO: Criando as variáveis com input 
    nome_aluno = input("Nome do aluno: ")
    telefone_aluno = input("Digite o telefone do aluno: ")
    turma_aluno = input("Digite a turma do aluno: ")
    idade_aluno = int(input("Digite a idade do aluno: "))
    cpf_aluno = input("Digite o CPF do aluno: ")
    id_professor = input("Digite o ID do professor: ")


    comando_inserir = (f'''
        INSERT INTO alunos (nome,telefone,turma,idade,cpf,id_professor)
        VALUES ('{nome_aluno}','{telefone_aluno}','{turma_aluno}',{idade_aluno},'{cpf_aluno}','{id_professor}')''')

    cursor.execute(comando_inserir)
    conexao.commit()
    conexao.close()

def listar_aluno():
    conexao = sqlite3.connect("escola_demonstracao.db")
    cursor = conexao.cursor ()
    cursor.execute('''SELECT * FROM alunos''')
    todos_alunos = cursor.fetchall()
    if not todos_alunos: 
        print("nenhum aluno cadastrado")
    else:
        for aluno in todos_alunos:
            print (f"ID: {aluno[0]}, nome: {aluno[1]}, Telefone: {aluno[2]}, turma: {aluno[3]}, idade: {aluno[4]}, CPF: {aluno[5]}, ID: {aluno[6]}")
        
    conexao.close()

def alterar_aluno ():
    
    conexao = sqlite3.connect("escola_demonstracao.db")
    cursor = conexao.cursor()

    id_acesso = int(input("Digite o ID: "))

    cursor.execute (f"SELECT * FROM alunos WHERE id = {id_acesso}")

    aluno = cursor.fetchone()

    if not aluno:
        print("Aluno não encontrado!")

        conexao.close()
        return
    
    else:
        novo_nome = input("Digite o nome: ")
        novo_telefone =input("Digite o telefone : ")
        nova_idade = int(input("Digite a sua idade: "))
        nova_turma = input("Digite sua nova turma: ")
        novo_cpf = input("Digite o CPF: ")
        id_professor_novo = input("Digite o ID do professor para alterar: " )
  
        comando = (f'''
        UPDATE alunos SET nome=  '{novo_nome}',
        telefone= '{novo_telefone}',
        idade= {nova_idade},
        turma= '{nova_turma}',
        cpf= '{novo_cpf}',
        id_professor = {id_professor_novo}
        WHERE id = {id_acesso}
        ''')
        
        cursor.execute(comando)
        conexao.commit()
        print("Aluno alterado!")
        conexao.close()

def excluir_aluno ():
    conexao = sqlite3.connect("escola_demonstracao.db")
    cursor = conexao.cursor() 

    listar_aluno()

    id_remover = int(input("Digite o ID: "))

    cursor.execute(f''' DELETE FROM alunos WHERE id = {id_remover}''')

    conexao.commit()

    print("Aluno removido com sucesso!") 
    conexao.close()


def menu():
     while True:
        print(" SISTEMA DE ALUNOS! ")
        print("1. Cadastrar alunos!")
        print("2. Listar alunos!") 
        print("3. Atualizar alunos!")  
        print("4. Excluir alunos!") 
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1': cadastrar_aluno()  
        elif opcao == '2': listar_aluno()
        elif opcao == '3': alterar_aluno()  
        elif opcao == '4': excluir_aluno()
        elif opcao == '5' : break
        else: print("Opção inválida!")
        
menu()

