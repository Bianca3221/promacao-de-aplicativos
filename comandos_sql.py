import sqlite3
conexao = sqlite3.connect("escola_demonstracao.db")
cursor = conexao.cursor ()

cursor.execute(''' ALTER TABLE professores ADD COLUMN
               endereco TEXT''')


conexao.commit()
conexao.close()