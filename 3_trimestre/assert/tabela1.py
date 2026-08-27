import sqlite3


def criar_tabela():
    try:
        conexao = sqlite3.connect("parque.db")
        conexao.execute("PRAGMA foreign_keys = ON")
        cursor = conexao.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS corporacoes_entretenimento (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_grupo TEXT NOT NULL,
                pais_sede TEXT NOT NULL
            )
        ''')

        conexao.commit()

    except sqlite3.Error as erro:
        print("Erro ao criar tabela de corporações:", erro)

    finally:
        conexao.close()


def inserir():
    try:
        conexao = sqlite3.connect("parque.db")
        conexao.execute("PRAGMA foreign_keys = ON")
        cursor = conexao.cursor()

        nome = input("Digite o nome da corporação: ")
        pais = input("Digite o país da sede: ")

        cursor.execute('''
            INSERT INTO corporacoes_entretenimento
            (nome_grupo, pais_sede)
            VALUES (?, ?)
        ''', (nome, pais))

        conexao.commit()

        print("Corporação cadastrada com sucesso!")

    except sqlite3.Error as erro:
        print("Erro ao cadastrar corporação:", erro)

    finally:
        conexao.close()


def listar():
    try:
        conexao = sqlite3.connect("parque.db")
        conexao.execute("PRAGMA foreign_keys = ON")
        cursor = conexao.cursor()

        cursor.execute('''
            SELECT * FROM corporacoes_entretenimento
        ''')

        registros = cursor.fetchall()

        print("\n--- CORPORAÇÕES ---")

        if registros:
            for registro in registros:
                print(
                    f"ID: {registro[0]} | "
                    f"Nome: {registro[1]} | "
                    f"País: {registro[2]}"
                )
        else:
            print("Nenhuma corporação cadastrada.")

    except sqlite3.Error as erro:
        print("Erro ao listar corporações:", erro)

    finally:
        conexao.close()


def atualizar():
    try:
        listar()

        conexao = sqlite3.connect("parque.db")
        conexao.execute("PRAGMA foreign_keys = ON")
        cursor = conexao.cursor()

        id_corporacao = int(
            input("Digite o ID da corporação que deseja alterar: ")
        )

        novo_nome = input("Digite o novo nome da corporação: ")
        novo_pais = input("Digite o novo país da sede: ")

        cursor.execute('''
            UPDATE corporacoes_entretenimento
            SET nome_grupo = ?,
                pais_sede = ?
            WHERE id = ?
        ''', (novo_nome, novo_pais, id_corporacao))

        conexao.commit()

        if cursor.rowcount > 0:
            print("Corporação alterada com sucesso!")
        else:
            print("Corporação não encontrada.")

    except sqlite3.Error as erro:
        print("Erro ao atualizar corporação:", erro)

    finally:
        conexao.close()


def excluir():
    try:
        listar()

        conexao = sqlite3.connect("parque.db")
        conexao.execute("PRAGMA foreign_keys = ON")
        cursor = conexao.cursor()

        id_corporacao = int(
            input("Digite o ID da corporação que deseja remover: ")
        )

        cursor.execute('''
            SELECT * FROM corporacoes_entretenimento
            WHERE id = ?
        ''', (id_corporacao,))

        if cursor.fetchone():

            cursor.execute('''
                SELECT * FROM parques
                WHERE id_corporacoes = ?
            ''', (id_corporacao,))

            if cursor.fetchone():
                print(
                    "Não é possível excluir esta corporação "
                    "porque existem parques relacionados a ela."
                )
            else:
                cursor.execute('''
                    DELETE FROM corporacoes_entretenimento
                    WHERE id = ?
                ''', (id_corporacao,))

                conexao.commit()

                print("Corporação removida com sucesso!")

        else:
            print("Corporação não encontrada.")

    except sqlite3.Error as erro:
        print("Erro ao excluir corporação:", erro)

    finally:
        conexao.close()
