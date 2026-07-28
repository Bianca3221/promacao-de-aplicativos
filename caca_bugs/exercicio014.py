import sqlite3

def criar_serie_seguro (nome, id_escola):
    try:
        conexao = sqlite3.connect('sistema.db')
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO series (nome_series. id_escola) VALUES (?,?)"
(nome, id_escola))
        conexao.commit()
    except sqlite3.Error as e:
        print("Erro tecnico:", e)
    finally:
        if conexao:
            conexao.close()

# Tava dando erro por que a conexao pode dar erro no finally vai fechar algo que deu erro 
# Adicionamos o if conexao:

    