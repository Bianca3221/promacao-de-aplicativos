import sqlite3 
 
def criar_tabela_turma(): 
    conexao = sqlite3.connect('sistema_escola.db') 
    cursor = conexao.cursor() 
     
    cursor.execute(''' 
    	CREATE TABLE IF NOT EXISTS turmas ( 
        	id INTEGER PRIMARY KEY AUTOINCREMENT, 
            nome_turma TEXT, 
            id_serie INTEGER,  
        	FOREIGN KEY (id_serie) REFERENCES series(id) 
    	) 
	''') 
    conexao.commit() 
    conexao.close() 
# Falta o INTEGER por que toda a coluna de uma tabela precisa ter um tipo de dado