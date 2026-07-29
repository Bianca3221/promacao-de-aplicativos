import sqlite3

def buscar_dados_dinamicos(nome_tabela, id_registro):
    tabelas_permitidas = {"alunos", "turmas", "professores"}

    if nome_tabela not in tabelas_permitidas:
        raise ValueError("Nome de tabela inválido.")

    conexao = sqlite3.connect("sistema_escola.db")
    cursor = conexao.cursor()

    sql = f"SELECT * FROM {nome_tabela} WHERE id = ?"
    cursor.execute(sql, (id_registro,))

    print(cursor.fetchone())

    conexao.close()

# O valor do id continua sendo passado como parâmetro (?), evitando SQL Injection nessa parte da consulta.