import json

def criar_arquivo():
    open("matriculas.json", 'w').close()
    with open("matriculas.json", 'a') as arquivos:
        alunos = {"CPF" = cpf_aluno,
                  "Nome" = nome_aluno,
                  "turma" = turma_aluno,
                  "idade" = idade_aluno
                  }
