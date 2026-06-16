import sqlite3

def criar_tabela():
    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()

    cursor.execute('''
                    CREATE TABLE if NOT EXIST professores(
                        id INTEGER PRIMARY KEY AUTOINCREMENT
                        nome = TEXT NOT NULL,
                        telefone = TEXT,
                        materia = TEXT,
                        idade = INTEGER,
                        cpf = TEXT UNIQUE,
                        salario = TEXT,
                        nome_escola = TEXT ''')
    
    #informações para por na tabela
    nome_professor = input("Digite o nome do professor: ")
    telefone_professor = input("Digite o telefone do professor: ")
    materia_professor = input("Digite a matéria do professor: ")
    idade_professor = int(input("Digite a idade do professor: "))
    cpf_professor = input("Digite o CPF do professor: ")
    salario_professor = input("Digite o salário do professor: ")
    escola_professor = input("Digite o nome da escola: ")

    comando_inserir = f'''
        INSERT INTO alunos (nome,telefone,turma,idade,cpf)
        VALUES ('{nome_professor}','{telefone_professor}','{materia_professor}',{idade_professor},'{cpf_professor}','{salario_professor}','{escola_professor}')'''

def listar_alunos():
    conexao = sqlite3.connect("escola_demonstracao.db")
    cursor = conexao.cursor ()
    cursor.execute('''SELECT * FROM professores''')
    todos_professores = cursor.fetchall
    if not todos_professores:
        print("Nenhum professor cadastrado!")
    else:
        for professor in todos_professores:
            print(f"id = {professor[0]}, Nome = {professor[1]}, Telefone = {professor[2]}, Materia = {professor[3]}, Idade = {professor[4]},")
            