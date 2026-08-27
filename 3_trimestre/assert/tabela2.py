import sqlite3


def criar_tabela():
    try:
        conexao = sqlite3.connect("parque.db")
        conexao.execute("PRAGMA foreign_keys = ON")
        cursor = conexao.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS parques (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_parque TEXT NOT NULL,
                id_corporacoes INTEGER NOT NULL,
                FOREIGN KEY (id_corporacoes)
                REFERENCES corporacoes_entretenimento(id)
            )
        ''')

        conexao.commit()

    except sqlite3.Error as erro:
        print("Erro ao criar tabela de parques:", erro)

    finally:
        conexao.close()


def inserir():
    try:
        conexao = sqlite3.connect("parque.db")
        conexao.execute("PRAGMA foreign_keys = ON")
        cursor = conexao.cursor()

        nome = input("Digite o nome do parque: ")
        id_corporacao = int(
            input("Digite o ID da corporação: ")
        )

        cursor.execute('''
            SELECT * FROM corporacoes_entretenimento
            WHERE id = ?
        ''', (id_corporacao,))

        if cursor.fetchone():

            cursor.execute('''
                INSERT INTO parques
                (nome_parque, id_corporacoes)
                VALUES (?, ?)
            ''', (nome, id_corporacao))

            conexao.commit()

            print("Parque cadastrado com sucesso!")

        else:
            print("Corporação não encontrada.")

    except sqlite3.Error as erro:
        print("Erro ao cadastrar parque:", erro)

    finally:
        conexao.close()


def listar():
    try:
        conexao = sqlite3.connect("parque.db")
        conexao.execute("PRAGMA foreign_keys = ON")
        cursor = conexao.cursor()

        cursor.execute('''
            SELECT
                parques.id,
                parques.nome_parque,
                parques.id_corporacoes,
                corporacoes_entretenimento.nome_grupo
            FROM parques
            INNER JOIN corporacoes_entretenimento
            ON parques.id_corporacoes =
               corporacoes_entretenimento.id
        ''')

        registros = cursor.fetchall()

        print("\n--- PARQUES ---")

        if registros:
            for registro in registros:
                print(
                    f"ID: {registro[0]} | "
                    f"Parque: {registro[1]} | "
                    f"ID Corporação: {registro[2]} | "
                    f"Corporação: {registro[3]}"
                )
        else:
            print("Nenhum parque cadastrado.")

    except sqlite3.Error as erro:
        print("Erro ao listar parques:", erro)

    finally:
        conexao.close()


def atualizar():
    try:
        listar()

        conexao = sqlite3.connect("parque.db")
        conexao.execute("PRAGMA foreign_keys = ON")
        cursor = conexao.cursor()

        id_parque = int(
            input("Digite o ID do parque que deseja alterar: ")
        )

        novo_nome = input("Digite o novo nome do parque: ")

        novo_id_corporacao = int(
            input("Digite o novo ID da corporação: ")
        )

        cursor.execute('''
            SELECT * FROM corporacoes_entretenimento
            WHERE id = ?
        ''', (novo_id_corporacao,))

        if not cursor.fetchone():
            print("Corporação não encontrada.")
            conexao.close()
            return

        cursor.execute('''
            UPDATE parques
            SET nome_parque = ?,
                id_corporacoes = ?
            WHERE id = ?
        ''', (
            novo_nome,
            novo_id_corporacao,
            id_parque
        ))

        conexao.commit()

        if cursor.rowcount > 0:
            print("Parque alterado com sucesso!")
        else:
            print("Parque não encontrado.")

    except sqlite3.Error as erro:
        print("Erro ao atualizar parque:", erro)

    finally:
        conexao.close()


def excluir():
    try:
        listar()

        conexao = sqlite3.connect("parque.db")
        conexao.execute("PRAGMA foreign_keys = ON")
        cursor = conexao.cursor()

        id_parque = int(
            input("Digite o ID do parque que deseja remover: ")
        )

        cursor.execute('''
            SELECT * FROM parques
            WHERE id = ?
        ''', (id_parque,))

        if cursor.fetchone():

            cursor.execute('''
                DELETE FROM parques
                WHERE id = ?
            ''', (id_parque,))

            conexao.commit()

            print("Parque removido com sucesso!")

        else:
            print("Parque não encontrado.")

    except sqlite3.Error as erro:
        print("Erro ao excluir parque:", erro)

    finally:
        conexao.close()
