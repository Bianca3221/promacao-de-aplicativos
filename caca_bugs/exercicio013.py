import sqlite3

def verificar_registros():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM alunos")

    registros = cursor.fetchall()

    print(f"Primeiro print: {registros}",) # Se chamar non primeiro com o modo fetchall() busca todos os registros fazendo que no segundo print fique vazio
    print(f"segundo print: {registros}")

    conexao.close()

verificar_registros()
