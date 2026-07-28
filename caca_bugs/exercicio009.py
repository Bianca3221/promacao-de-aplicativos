import sqlite3

def atualizar_nome_aluno(id_aluno, novo_nome):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()
    
    cursor.execute("UPDATE alunos SET nome = ? WHERE id_aluno ", (novo_nome, id_aluno))

    # o erro é que faltava o WHERE no cursor execute, sem ele o banco atualiza todas as linhas na tabela
    # e tambem não chamou a função  "id_aluno" no cursor execute 

    conexao.commit()
    conexao.close()