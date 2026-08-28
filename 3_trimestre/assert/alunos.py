import sqlite3

def cadastrar_alunos(nome_aluno,idade_aluno,id_turma):
    try:
        conexao = sqlite3.connect('gestao_escolar.db')
        conexao.execute("PRAGMA foreign_keys = ON")
        cursor = conexao.cursor()

        cursor.execute(
            f"""
            INSERT INTO alunos (nome_aluno, idade_aluno, id_turma)
            VALUES ('{nome_aluno}', {idade_aluno}, {id_turma})
            """)
        
        conexao.commit()
        conexao.close()

        print("Aluno cadastrado com sucesso!")

    except sqlite3.IntegrityError:
        print("Erro: a turma informada não existe.")

    except sqlite3.Error as erro:
        print(f"Erro no banco de dados: {erro}")


def listar_aluno (alunos, aluno):
    try:
        conexao = sqlite3.connect('gestao_escolar.db')
        conexao.execute("PRAGMA foreign_keys = ON")
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM alunos")
        alunos = cursor.fetchall()

        conexao.close()

        print("\n--- ALUNOS ---")

        for aluno in alunos:
            print(
                f"ID: {aluno[0]} | "
                f"Nome: {aluno[1]} | "
                f"Idade: {aluno[2]} | "
                f"ID Turma: {aluno[3]}"
            )

    except sqlite3.Error as erro:
        print(f"Erro no banco de dados: {erro}")


def alterar_turmas (nome,idade,id_turma,id_aluno):
    try:
        conexao = sqlite3.connect('gestao_escolar.db')
        conexao.execute("PRAGMA foreign_keys = ON")
        cursor = conexao.cursor()

        cursor.execute(
            f"""
            UPDATE alunos
            SET nome = '{nome}',
                idade = {idade},
                id_turma = {id_turma}
            WHERE id = {id_aluno}
            """)

        conexao.commit()
        conexao.close()

        print("Aluno alterado com sucesso!")

    except sqlite3.IntegrityError:
        print("Erro: a turma informada não existe.")

    except sqlite3.Error as erro:
        print(f"Erro no banco de dados: {erro}")



def excluir_turmas(id_aluno):
    try:
        conexao = sqlite3.connect('gestao_escolar.db')
        conexao.execute("PRAGMA foreign_keys = ON")
        cursor = conexao.cursor() 

        cursor.execute(
            f"""
            DELETE FROM alunos
            WHERE id = {id_aluno}
            """) 

        conexao.commit()
        conexao.close()

        print("Aluno excluído com sucesso!")

    except sqlite3.Error as erro:
        print(f"Erro no banco de dados: {erro}")      



