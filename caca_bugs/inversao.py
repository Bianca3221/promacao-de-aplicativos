import sqlite3

def criar_tabelas():
    conexao = sqlite3.connect ('sistema_escola.db')
    cursor = conexao.cursor()
    cursor.execute('''
        CREAT TABLE IF NOT EXISTS escolas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT 
        )
     ''')

    cursor.execute('''
        CREAT TABLE IF NOT EXISTS series (
            id INTERGER PRIMERY KEY AUTOINCREMENT,
            nome_serie TEXT,
            id_escola INTEGER,
            FOREIGN KEY (id_escola) REFERENCES escola(id)
        )
    ''')

# puxa uma tabela pegando o id que não existe (por isso trava), inverter as tabelas 

    conexao.commit()
    conexao.close()