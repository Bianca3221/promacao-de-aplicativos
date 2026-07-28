import sqlite3 
 
def inserir_professor(nome, materia, cpf): 
    try: 
        conexao = sqlite3.connect('sistema_escola.db') 
        cursor = conexao.cursor() 
        cursor.execute("INSERTO INTO professores (nome, materia, cpf) VALUES (?,?,?)", (nome, materia, cpf)) 
        conexao.commit() 
    except sqlite3.Error: 
        print("Erro: Este CPF já está cadastrado no sistema!") 
    except sqlite3.Error as e:
        print("Erro no banco de dados:", e)
    finally:
        conexao.close()

        # O (INSERTO)  esta errado o correto é INSERT 
        # O Sqlite3.Error, ele captura qualquer erro, o mais correto seria especificar melhor o erro 
