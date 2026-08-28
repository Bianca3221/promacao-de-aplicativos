import sqlite3

def cadastrar_turma(nome_turma, id_escola):
    try:
        conexao = sqlite3.connect('gestao_escolar.db')
        conexao.execute("PRAGMA foreign_keys = ON")
        cursor = conexao.cursor()

        cursor.execute(
            f"""
            INSERT INTO turmas (nome_turma, id_escola)
            VALUES ('{nome_turma}', {id_escola})
            """)
        
        conexao.commit()
        conexao.close()

        print("Turma cadastrada com sucesso!")

    except sqlite3.IntegrityError:
        print("Erro: a escola informada não existe.")

    except sqlite3.Error as erro:
        print(f"Erro no banco de dados: {erro}")


def listar_turma(turma, turmas):
    try:
        conexao = sqlite3.connect('gestao_escolar.db')
        conexao.execute("PRAGMA foreign_keys = ON")
        cursor = conexao.cursor()

        cursor.execute ("SELECT * FROM turmas")
        turmas = cursor.fetchall()

        conexao.close()

        if not turmas:
            print("Nenhuma turma cadastrada.")
            return
        
        print("\n--- TURMAS ---")

        for turma in turmas:
            print(
                f"ID: {turma[0]} | "
                f"Turma: {turma[1]} | "
                f"ID Escola: {turma[2]}"
            )
    except sqlite3.Error as erro:
        print(f"Erro no banco de dados: {erro}")


def alterar_turma (nome_turma, id_escola, id_turma):
    try:
        conexao = sqlite3.connect('gestao_escolar.db')
        conexao.execute("PRAGMA foreign_keys = ON")
        cursor = conexao.cursor()

        cursor.execute(
            f"""
            UPDATE turmas
            SET nome_turma = '{nome_turma}',
                id_escola = {id_escola}
            WHERE id = {id_turma}
            """)
        
        conexao.commit()
        conexao.close()

        print("Turma alterada com sucesso!")

    except sqlite3.IntegrityError:
        print("Erro: a escola informada não existe.")

    except sqlite3.Error as erro:
        print(f"Erro no banco de dados: {erro}")



def excluir_turma(id_turma):
    try:
        conexao = sqlite3.connect('gestao_escolar.db')
        conexao.execute("PRAGMA foreign_keys = ON")
        cursor = conexao.cursor()

        cursor.execute(
            f"DELETE FROM turmas WHERE id = {id_turma}")
        
        conexao.commit()
        conexao.close()

        print("Turma excluída com sucesso!")

    except sqlite3.IntegrityError:
        print(
            "Não é possível excluir a turma, "
            "pois existem alunos vinculados a ela."
        )

    except sqlite3.Error as erro:
        print(f"Erro no banco de dados: {erro}")

        




        