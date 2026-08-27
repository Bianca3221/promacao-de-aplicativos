def calcular_desconto(preco, percentual):
 	return preco - percentual

assert calcular_desconto(100, 10) == 90
assert calcular_desconto(200, 20) == 160
assert calcular_desconto(50, 10) == 45 

# Função corrigida:
def calcular_desconto(preco, percentual):
    desconto = preco * percentual / 100
    return preco - desconto


# Executando novamente os testes após a correção:
assert calcular_desconto(100, 10) == 90
assert calcular_desconto(200, 20) == 160
assert calcular_desconto(50, 10) == 45

