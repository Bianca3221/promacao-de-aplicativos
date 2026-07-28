import sqlite3
def cadastar_serie(nome_serie, id_escola):
    conexao =sqlite3.connect('sistema_escola.db')
    conexao.execute("PRAGMAN foreign_key = ON")
    cursor = conexao.cursor()
    try:
        cursor.execute("INSERT INTO series (nome_serie, id_escola) VALUES (?, ?)",
(nome_serie, id_escola))
        conexao.commit()
    except sqlite3.IntegrityError:
        print("Erro: Escola inexistente!")
    finally:
        conexao.close()

# Falta o conexao.execute("PRAGMAN foreign_key = ON"), faz verificar se o id_escola existe na tabela escola. 