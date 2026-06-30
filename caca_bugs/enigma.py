import sqlite3

def buscar_professor(id_prof):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT nome FROM professores WHERE Id = ?", (id_prof,)) # Faltou a (,), pois se não ele nao entende como parâmetro 
    resultado = cursor.fetchone()
    print(resultado)
    conexao.close()