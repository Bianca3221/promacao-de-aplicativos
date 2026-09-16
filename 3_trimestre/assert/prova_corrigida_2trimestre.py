import sqlite3


def criar_tabela_corporacoes():
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


def criar_tabela_parques():
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


def inserir_corporacao():
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


def inserir_parque():
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
            print("Erro! Corporação não encontrada.")

    except sqlite3.Error as erro:
        print("Erro ao cadastrar parque:", erro)

    finally:
        conexao.close()


def listar_corporacoes():
    try:
        conexao = sqlite3.connect("parque.db")
        conexao.execute("PRAGMA foreign_keys = ON")
        cursor = conexao.cursor()

        cursor.execute('''
            SELECT * FROM corporacoes_entretenimento
        ''')

        registros = cursor.fetchall()

        if registros:
            print("\n--- CORPORAÇÕES ---")

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


def listar_parques():
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
            ON parques.id_corporacoes = corporacoes_entretenimento.id
        ''')

        registros = cursor.fetchall()

        if registros:
            print("\n--- PARQUES ---")

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


def atualizar_corporacao():
    try:
        listar_corporacoes()

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


def atualizar_parque():
    try:
        listar_parques()

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
        ''', (novo_nome, novo_id_corporacao, id_parque))

        conexao.commit()

        if cursor.rowcount > 0:
            print("Parque alterado com sucesso!")
        else:
            print("Parque não encontrado.")

    except sqlite3.Error as erro:
        print("Erro ao atualizar parque:", erro)

    finally:
        conexao.close()


def excluir_corporacao():
    try:
        listar_corporacoes()

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
                    "Não é possível excluir esta corporação, "
                    "pois existem parques relacionados a ela."
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
        print("Erro ao remover corporação:", erro)

    finally:
        conexao.close()


def excluir_parque():
    try:
        listar_parques()

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
        print("Erro ao remover parque:", erro)

    finally:
        conexao.close()


def menu():
    while True:

        print("\n========== MENU ==========")
        print("1. Cadastrar Corporação")
        print("2. Cadastrar Parque")
        print("3. Listar Corporações")
        print("4. Listar Parques")
        print("5. Atualizar Corporação")
        print("6. Atualizar Parque")
        print("7. Excluir Corporação")
        print("8. Excluir Parque")
        print("9. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            inserir_corporacao()

        elif opcao == '2':
            inserir_parque()

        elif opcao == '3':
            listar_corporacoes()

        elif opcao == '4':
            listar_parques()

        elif opcao == '5':
            atualizar_corporacao()

        elif opcao == '6':
            atualizar_parque()

        elif opcao == '7':
            excluir_corporacao()

        elif opcao == '8':
            excluir_parque()

        elif opcao == '9':
            print("Programa encerrado!")
            break

        else:
            print("Opção inválida!")

criar_tabela_corporacoes()
criar_tabela_parques()

menu()
