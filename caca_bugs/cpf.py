import sqlite3

def cadastrar_professor(nome,cpf):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute('''
            CREAT TABLE if NOT EXIST professores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                cpf TEXT UNIQUE.
                   ) ''')
    # Faltou o UNIQUE para demontrar que o CPF é unico
    conexao.commit()
    conexao.close()