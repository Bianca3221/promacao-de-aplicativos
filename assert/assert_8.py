def buscar_nome(lista, nome):
    return nome in lista


def tem_senha_valida(senha):
    return len(senha) >= 8


# Testes para buscar_nome
assert buscar_nome([], "Ana") == False         
assert buscar_nome(["Ana", "João"], "Ana") == True
assert buscar_nome(["Ana", "João"], "Maria") == False


# Testes para tem_senha_valida
assert tem_senha_valida("1234567") == False    
assert tem_senha_valida("12345678") == True     
assert tem_senha_valida("123456789") == True    
