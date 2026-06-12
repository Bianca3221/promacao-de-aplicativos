import sqlite3

def cadastrar_aluno() :
    # 1. CONEXÃO: Abre ou cria o arquivo do banco de dados import sqlite3
    conexao = sqlite3.connect("escola_demonstracao.db")
    cursor = conexao.cursor ()

    # 2 passo CRIAÇÃO DA TABELA 
    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS alunos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        telefone TEXT,
                        turma TEXT,
                        idade INTEGER,
                        cpf TEXT UNIQUE NOT NULL
                )
                ''')

    # 3. INFORMAÇÕES DO ALUNO: Criando as variáveis com input 
    nome_aluno = input("Nome do aluno: ")
    telefone_aluno = input("Digite o telefone do aluno: ")
    turma_aluno = input("Digite a turma do aluno: ")
    idade_aluno = int(input("Digite a idade do aluno: "))
    cpf_aluno = input("Digite o CPF do aluno: ")


    comando_inserir = f'''
        INSERT INTO alunos (nome,telefone,turma,idade,cpf)
        VALUES ('{nome_aluno}','{telefone_aluno}','{turma_aluno}',{idade_aluno},'{cpf_aluno}')'''

    cursor.execute(comando_inserir)
    conexao.commit()
    conexao.close()

def listar_alunos():
    conexao = sqlite3.connect("escola_demonstracao.db")
    cursor = conexao.cursor ()
    cursor.execute('''SELECT * FROM alunos''')
    todos_alunos = cursor.fetchall()
    if not todos_alunos: 
        print("nenhum aluno cadastrado")
    else:
        for aluno in todos_alunos:
            print (f"ID: {aluno[0]}, nome: {aluno[1]}, Telefone: {aluno[2]}, turma: {aluno[3]}, idade: {aluno[4]}, CPF: {aluno[5]}")
        
    conexao.close()

listar_alunos()

def alterar_aluno ():
    
    conexão = sqlite3.connect("escola_demonstracao.db")
    cursor = conexão.cursor()

    id_acesso = int(input("Digite o ID: "))
    novo_nome = input("Digite o nome da alteração:")
    novo_cpf = input("Digite o novo CPF: ")


    cursor.execute (f"UPDATE alunos SET nome = '{novo_nome}', cpf = '{novo_cpf}' WHERE id = {id_acesso};")

    conexão.commit()

    print("Dados atualizados com sucesso!")
    conexão.close()


def exclui_aluno ():
    