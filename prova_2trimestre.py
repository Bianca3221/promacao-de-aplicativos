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
        print("Erro ao criar o banco:", erro)

    finally:
        conexao.close()


def inserir_tabela():
    try:
        conexao = sqlite3.connect("parque.db")
        conexao.execute("PRAGMA foreign_keys = ON")
        cursor = conexao.cursor()

        nome_entretenimento = input("Digite o nome do entretenimento: ")
        pais_entretenimento = input("Digite o país: ")
        nome_parque = input("Digite o nome do parque: ")
        id_entretenimento = int(input("Digite o ID do entretenimento: "))

        comando_inserir = f'''
            INSERT INTO corporacoes_entretenimento
            (nome_grupo, pais_sede)
            VALUES ('{nome_entretenimento}', '{pais_entretenimento}')
        '''

        cursor.execute(comando_inserir)
        conexao.commit()

        cursor.execute(f'''
            SELECT * FROM corporacoes_entretenimento
            WHERE id = {id_entretenimento}
        ''')

        if cursor.fetchone():

            comando_inserir = f'''
                INSERT INTO parques
                (nome_parque, id_corporacoes)
                VALUES ('{nome_parque}', '{id_entretenimento}')
            '''

            cursor.execute(comando_inserir)
            conexao.commit()

            print("Parque cadastrado com sucesso!")

        else:
            print("Erro! Entretenimento não encontrado.")

    except sqlite3.Error as erro:
        print("Erro:", erro)

    finally:
        conexao.close()


def listar():
    try:
        conexao = sqlite3.connect("parque.db")
        conexao.execute("PRAGMA foreign_keys = ON")
        cursor = conexao.cursor()

        cursor.execute('''
            SELECT * FROM parques
        ''')

        registros = cursor.fetchall()

        for registro in registros:
            print(registro)

    except sqlite3.Error as erro:
        print("Erro:", erro)

    finally:
        conexao.close()


def atualizar():
    try:
        listar()

        conexao = sqlite3.connect("parque.db")
        conexao.execute("PRAGMA foreign_keys = ON")
        cursor = conexao.cursor()

        id_parque = int(input("Digite o ID do parque que deseja alterar: "))

        novo_nome = input("Digite o novo nome do parque: ")
        novo_id_corporacao = int(
            input("Digite o novo ID da corporação: ")
        )
        novo_pais = input("Digite o novo país da sede: ")

        cursor.execute(f'''
            UPDATE parques
            SET nome_parque = '{novo_nome}',
                id_corporacoes = '{novo_id_corporacao}'
            WHERE id = '{id_parque}'
        ''')

        cursor.execute(f'''
            UPDATE corporacoes_entretenimento
            SET pais_sede = '{novo_pais}'
            WHERE id = '{novo_id_corporacao}'
        ''')

        conexao.commit()

        print("Dados alterados com sucesso!")

    except sqlite3.Error as erro:
        print("Erro ao atualizar:", erro)

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

        cursor.execute(f'''
            SELECT * FROM parques
            WHERE id = {id_parque}
        ''')

        if cursor.fetchone():

            cursor.execute(f'''
                DELETE FROM parques
                WHERE id = {id_parque}
            ''')

            conexao.commit()

            print("Parque removido com sucesso!")

        else:
            print("Parque não encontrado.")

    except sqlite3.Error as erro:
        print("Erro ao remover:", erro)

    finally:
        conexao.close()


def menu():
    while True:
        print("\n1. Cadastrar Parques")
        print("2. Listar Parques")
        print("3. Atualizar Parques")
        print("4. Excluir Parques")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            inserir_tabela()

        elif opcao == '2':
            listar()

        elif opcao == '3':
            atualizar()

        elif opcao == '4':
            excluir()

        elif opcao == '5':
            break

        else:
            print("Opção inválida!")


criar_tabela()
menu()
