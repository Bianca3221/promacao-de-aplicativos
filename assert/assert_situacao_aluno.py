def situacao_aluno(media):
    if media >= 6:
        return "Aprovado"
    return "Reprovado"

assert situacao_aluno(8) == "Aprovado"

 # Crie testes para as médias: 6, 5.9, 0 e 10.

# Explique por que 6 e 5.9 são chamados de casos de limite.
#R= 6 por que é a nota minima para ser aprovado, 5.9 é menor que 6 então não entra no requisito de "Aprovado".

assert situacao_aluno(6) == "Aprovado"
assert situacao_aluno(5.9) == "Reprovado"
assert situacao_aluno(0) == "Reprovado"
assert situacao_aluno(10) == "Aprovado"


