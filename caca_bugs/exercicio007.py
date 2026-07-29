import sqlite3

def cadastrar_turma (nome, id_serie, id_prof) :
    conexao = sqlite3.connect('sistema_escola.db')
    try:
        cursor = conexao.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;")
        cursor.execute("INSERT INTO turmas (nome_turma, id_serie, id_professor) VALUES (?, ?, ?)",(nome , id_serie, id_serie, id_prof))
    except sqlite3.IntegrityError:
        print("Não existe o professor informado")
        conexao.commit()
    finally:
        conexao.close()
#Não tem o try para executar o except e nem o finally
# o conexao.close() não sera executado
