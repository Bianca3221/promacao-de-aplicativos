import sqlite3
conexao = sqlite3.connect('escola_demonstracao.db')
cursor = conexao.cursor ()
cursor.execute('''ALTERAR TABLE alunos ADD COLUMN
               cidade_estado TEXT ''')
