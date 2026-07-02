import sqlite3

def inserir_escola (nome):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO escolas (nome) VALUES (?)", (nome,))
    conexao.commit()
    conexao.commit() 
    # O erro foi que não abriu o arquivo dentro da def fazendo com que o programa não seja executado