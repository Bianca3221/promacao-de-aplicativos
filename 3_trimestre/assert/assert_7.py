# FUNÇÃO ORIGINAL COM ERRO
def eh_par(numero):
    return numero % 2 == 1

assert eh_par(2) == True
assert eh_par(3) == False
assert eh_par(10) == True


# FUNÇÃO CORRIGIDA
def eh_par(numero):
    return numero % 2 == 0


# TESTES APÓS A CORREÇÃO
assert eh_par(2) == True
assert eh_par(3) == False
assert eh_par(10) == True

print("Todos os testes passaram!")
    

# Explicação: A função original estava errada porque verificava se o resto da divisão por 2 era 1. Para um número ser par,
# o resto precisa ser 0. Por isso, a correção foi trocar == 1 por == 0.