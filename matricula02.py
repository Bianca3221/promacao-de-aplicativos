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

def atualizar ():
    print("----ATUALIZAR-----")
    if not os.path.exists(MATRICULA):
         print("Nenhum aluno cadastrado no sistema.") 
         return
    
    with open(MATRICULA, 'r', encoding='utf-8') as f: 
        alunos  = json.load(f)

    cpf_busca = int(input("Digite o CPF do aluno que deseja editar: "))
    
    for aluno in alunos:
        if aluno['cpf'] == cpf_busca: 
            print(f"Editando dados de: {aluno['nome']}")
            aluno['nome'] = input(f"Novo Nome ({aluno['nome']}): ") or aluno['nome']
            aluno['telefone'] = input(f"Novo Telefone ({aluno['telefone']}): ") or aluno['telefone']
            aluno['turma'] = input(f"Nova Turma ({aluno['turma']}): ") or aluno['turma']
            aluno['idade'] = int(input(f"Nova Idade ({aluno['idade']}): ") or aluno['idade'])
            aluno['cpf'] = input(f"Novo CPF ({aluno['cpf']}): ") or aluno['cpf']

            with open(MATRICULA, 'w', encoding='utf-8') as f:    
                json.dump(alunos, f, indent=4, ensure_ascii=False)   
            print("Dados atualizados com sucesso!")
            return
        
    print("Aluno não encontrado.")


def excluir():
    print("\n--- Excluir Aluno ---")
    if not os.path.exists(MATRICULA):
        print("Nenhum aluno cadastrado no sistema.")
        return
    with open (MATRICULA, 'r', encoding='utf-8') as f:
        alunos = json.load(f) 

    id_busca = int(input("Digite o ID do aluno que deseja remover: "))

    nova_lista = [a for a in alunos if a['id'] != id_busca]
    
    if len(nova_lista) < len(alunos):
        with open(MATRICULA, 'w', encoding='utf-8') as f:
             json.dump([], f)

def menu():
    while True:
        print("\n=== SISTEMA ESCOLAR ===") 
        print("1. Cadastrar Aluno")
        print("2. Listar Alunos") 
        print("3. Atualizar Aluno")  
        print("4. Excluir Aluno") 
        print("5. Sair") 

        opcao = input("Escolha uma opção: ")

        if opcao == '1': cadastrar()  
        elif opcao == '2': listar()
        elif opcao == '3': atualizar()  
        elif opcao == '4': excluir()
        elif opcao == '5': break 
        else: print("Opção inválida!")
 
menu()
    


        
    
    

