def buscar_nome(lista, nome):
 	return nome in lista

def tem_senha_valida(senha):
 	return len(senha) >= 8

 # Escreva os asserts abaixo.
assert buscar_nome([], "Ana") == False          # lista vazia
assert buscar_nome(["Ana", "João"], "Ana") == True
assert buscar_nome(["Ana", "João"], "Carlos") == False

# tem_senha_valida
assert tem_senha_valida("") == False             # senha vazia
assert tem_senha_valida("1234567") == False      # limite abaixo de 8
assert tem_senha_valida("12345678") == True      # limite: exatamente 8 caracteres

# O que acontece ao buscar um nome em uma lista vazia?
# Ao buscar um nome em uma lista vazia, o resultado é False, porque a lista não contém nenhum nome.
