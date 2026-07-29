import sqlite3
def criar_tabela():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute('''
                    CREATE TABLE if NOT EXISTS turmas(
                        nome_turma TEXT NOT NULL,
                        id_serie INTEGER PRIMARY KEY AUTOINCREMENT,
                        id_serie INTEGER PRIMARY KEY AUTOINCREMENT,) ''')
        