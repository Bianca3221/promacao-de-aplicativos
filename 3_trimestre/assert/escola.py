import sqlite3
from banco import conectar


def cadastrar_escola(nome, cidade):
    try:
        conexao = sqlite3.connect('gestao_escolar.db')
        conexao.execute("PRAGMA foreign_keys = ON")
        cursor = conexao.cursor()

        cursor.execute(
            f"INSERT INTO escolas (nome, cidade) VALUES ('{nome}', '{cidade}')"
        )    
        conexao.commit()
        conexao.close()

        print("Escola cadastrada com sucesso!")

    except sqlite3.Error as erro:
        print(f"Erro no banco de dados: {erro}")


def listar_escolas(escolas,escola):
    try:
        conexao = sqlite3.connect('gestao_escolar.db')
        conexao.execute("PRAGMA foreign_keys = ON")
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM escolas")
        escolas = cursor.fetchall()

        conexao.close()

        if not escolas:
            print("Nenhuma escola cadastrada.")
            return

        for escola in escolas:
            print(
                f"ID: {escola[0]} | "
                f"Nome: {escola[1]} | "
                f"Cidade: {escola[2]}"
            )
        
    except sqlite3.Error as erro:
        print(f"Erro ao listar escolas: {erro}")

def alterar_escola(id_escola, nome, cidade):
    try: 
        conexao = sqlite3.connect('gestao_escolar.db')
        conexao.execute("PRAGMA foreign_keys = ON")
        cursor = conexao.cursor() 

        cursor.execute  (f"""
            UPDATE escolas
            SET nome = '{nome}', cidade = '{cidade}'
            WHERE id = {id_escola}
            """)
        
        conexao.commit()
        conexao.close()
        
        print("Escola alterada com sucesso!")

    except sqlite3.Error as erro:
        print(f"Erro no banco de dados: {erro}")


def excluir_escola(id_escola):
    try:
        conexao = sqlite3.connect('gestao_escolar.db')
        conexao.execute("PRAGMA foreign_keys = ON")
        cursor = conexao.cursor()

        cursor.execute(
            f"""
            DELETE FROM escolas
            WHERE id = {id_escola}
            """
        )

        conexao.commit()
        conexao.close()

        print("Escola excluída com sucesso!")

    except sqlite3.IntegrityError:
        print("Não é possível excluir a escola, pois existem turmas vinculadas a ela.")

    except sqlite3.Error as erro:
        print(f"Erro no banco de dados: {erro}")
