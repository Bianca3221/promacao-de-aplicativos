import sqlite3

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

cursor.execute('''SELECT * FROM alunos''')
todos_alunos = cursor.fetchall()
if not todos_alunos: 
    print (f"Nome{nome_aluno[0]},Tefone:{telefone_aluno[1]},Telefone:{telefone_aluno[2]},Idade:{idade_aluno[3]},CPF:{cpf_aluno[4]}")
conexao.close()

