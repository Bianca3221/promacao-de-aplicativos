import sqlite3

def cadastrar_escola_manual():
    id_escola = int(input("Digite o ID para a nova escola: "))
    nome = input("Nome da escola: ")

    conexao = sqlite3.connect("sistema_escola.db")
    cursor = conexao.cursor()

    try:
        cursor.execute(
            "INSERT INTO escolas (id, nome) VALUES (?, ?)",
            (id_escola, nome)
        )
        conexao.commit()
        print("Escola cadastrada com sucesso!")

    except sqlite3.IntegrityError:
        print("Erro: já existe uma escola cadastrada com esse ID.")

    finally:
        conexao.close()

# Não existe tratamento de erro para o ID duplicado, por isso colocar o sqlite3.InteregrityError 