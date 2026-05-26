import json
import os 

MATRICULA = 'alunos.json'

def cadastrar():
    print("-----CADASTRO-----")

    if os.path.exists(MATRICULA):
        with open (MATRICULA, 'r', encoding='utf-8') as f: 
            alunos = json.load(f)

    else: 
        alunos = []
    id_aluno = int(input("ID do aluno :"))
    
    novo_aluno = {
        "id" :  id_aluno,
        "nome" : input("Nome: "),
        "telefone" : input("Telefone: "),
        "turma" : input("Turma do aluno: "),
        "idade" : int(input("Idade: ")),
        "cpf" : input("CPF: ")
    }

    if len(alunos) !=0 :
        for dado in alunos:
            if dado("id")  == id_aluno :
                print("ID cadastrado!")
                return
    
    alunos.append(novo_aluno)
    with open (MATRICULA, 'w' ) as f :
        json.dump(alunos, f, indent=4, ensure_ascii=False)

    print("Aluno cadastrado com sucesso")
          
def listar():
    print("-----LISTAR-----")
    if os.path.exists(MATRICULA):
        with open(MATRICULA, 'w', encoding='utf-8') as f:
            alunos = json.load(f)
        
    else: 
        alunos = []

    if not alunos:
        print("Nenhum aluno cadastrado!")
        return
    
    for aluno in alunos: 
        print(f"Nome: {aluno['nome']} | CPF: {aluno['cpf']} | Turma: {aluno['turma']} | Tel: {aluno['telefone']}")

        
        
    
    

