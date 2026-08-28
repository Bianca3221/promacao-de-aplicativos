import sqlite3

def criar_tabela ():
    try:
        conexao = sqlite3.connect ('gestao_escolar.db')
        conexao.execute("PRAGMA foreign_keys = ON")
        cursor = conexao.cursor()
        
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS escolas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_escola TEXT NOT NULL,
            nome_cidade TEXT NOT NULL
            )
            ''')
        
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS turmas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_turma TEXT NOT NULL,
            id_escola  INTEGER NOT NULL,
            FOREIGN KEY (id_escola) REFERENCES escolas(id)
            )
            ''')
        
        cursor.execute('''
        CREAT TABLE IF NOT EXISTS alunos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_aluno TEXT NOT NULL,
        idade_aluno INTEGER NOT NULL,
        id_turma INTEGER NOT NULL,
        FOREIGN KEY (id_turma) REFERENCES turmas(id)
        ) 
        ''')

        conexao.commit()


        print("Tabelas criadas com sucesso!")

    except sqlite3.Error as erro:
        print(f"Erro no banco de dados: {erro}")
    finally:
        if conexao is not None:
            conexao.close()

