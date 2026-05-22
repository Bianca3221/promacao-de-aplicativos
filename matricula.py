import json
# Para armazenar e saber que é um arquivo JSON
import os
# Uma biblioteca padrão muito útil, para não carregar os erros e explodi 

BANCO_DADOS = 'alunos.json'
# 'alunos.json' é o arquivo que vamos utilizar  

def cadastrar():
    # Def: cria a função 
    print("\n--- Novo Cadastro ---")
    # esse print é utilizado para deixar o codigo com a estetica bonita
    if os.path.exists(BANCO_DADOS):
    # if:se, os.path: Verificar e montar caminhos exists: retorna False (BANCO_DADOS): arquivo
        with open(BANCO_DADOS, 'r', encoding='utf-8') as f:
        # para abrir o arquivo em modo leitura
            alunos = json.load(f)
        # para carregar oque tem dentro do arquivo
    else:
        # se não
        alunos = []
        #lista vazia 

    novo_aluno = { #inicio para saber que é um objeto 
        "nome": input("Nome: "), # caracteristica do objeto e input: Para pedir o valor da variavél
        "telefone": input("Telefone: "), # caracteristica do objeto e input: Para pedir o valor da variavél
        "turma": input("Turma: "),  # caracteristica do objeto e input: Para pedir o valor da variavél
        "idade": int(input("Idade: ")),  # caracteristica do objeto e input: Para pedir o valor da variavél, int: para o sistema entender que é numero inteiro
        "cpf": input("CPF: ") #caracteristica do objeto e input: Para pedir o valor da variavél, não tem a vírgula pois não tem mais caracteristica
    }
    
    alunos.append(novo_aluno)
    # Adicionar um novo aluno na lista de novo_aluno 

    with open(BANCO_DADOS, 'w', encoding='utf-8') as f: # abrir arquivo no modo rescrever, encoding : formatação
        json.dump(alunos, f, indent=4, ensure_ascii=False) # carregar arquivo 
        
    print("Aluno cadastrado com sucesso!") # print de aprovação

def listar(): # nova função
    print("\n--- Lista de Alunos ---") #esse print é utilizado para deixar o codigo com a estetica bonita
    
    if os.path.exists(BANCO_DADOS): # if:se, os.path: Verificar e montar caminhos exists: retorna False (BANCO_DADOS): arquivo
        with open(BANCO_DADOS, 'r', encoding='utf-8') as f:# arquivo no modo leitura, encoding='utf-8': formatação
            alunos = json.load(f) #Carregar arquivo
    else: # se não
        alunos = [] # Lista vazia

    if not alunos: # se nao alunos 
        print("Nenhum aluno cadastrado.") # print para mostrar alunos não cadastrado
        return # retorna em uma variavél 

    for aluno in alunos: # Percore a lista 
        print(f"Nome: {aluno['nome']} | CPF: {aluno['cpf']} | Turma: {aluno['turma']} | Tel: {aluno['telefone']}") 
    # Print usando as variaveis por isso as {} e o f para colocar a variavel
def atualizar(): # função
    print("\n--- Atualizar Aluno ---") #esse print é utilizado para deixar o codigo com a estetica bonita
    if not os.path.exists(BANCO_DADOS): # if:se, os.path: Verificar e montar caminhos exists: retorna False (BANCO_DADOS): arquivo
        print("Nenhum aluno cadastrado no sistema.") # print para mostrar alunos não cadastrado, retorna em uma variavél 
        return

    with open(BANCO_DADOS, 'r', encoding='utf-8') as f: # arquivo no modo leitura, encoding='utf-8': formatação
        alunos = json.load(f)  #Carregar arquivo
        
    cpf_busca = int(input("Digite o CPF do aluno que deseja editar: ")) # Variável  
    
    for aluno in alunos: # Percorrer 
        if aluno['cpf'] == cpf_busca: # mostrando qua a caracteristica foi substituida pelo input 
            print(f"Editando dados de: {aluno['nome']}") # print para mostrar que os dados foram atuliazados 
            aluno['nome'] = input(f"Novo Nome ({aluno['nome']}): ") or aluno['nome'] # Print usando as variaveis por isso as {} e o f para colocar a variavel
            aluno['telefone'] = input(f"Novo Telefone ({aluno['telefone']}): ") or aluno['telefone']# Print usando as variaveis por isso as {} e o f para colocar a variavel
            aluno['turma'] = input(f"Nova Turma ({aluno['turma']}): ") or aluno['turma']# Print usando as variaveis por isso as {} e o f para colocar a variavel
            aluno['idade'] = int(input(f"Nova Idade ({aluno['idade']}): ") or aluno['idade'])# Print usando as variaveis por isso as {} e o f para colocar a variavel
            aluno['cpf'] = input(f"Novo CPF ({aluno['cpf']}): ") or aluno['cpf']# Print usando as variaveis por isso as {} e o f para colocar a variavel
            
            with open(BANCO_DADOS, 'w', encoding='utf-8') as f:  # arquivo no modo leitura, encoding='utf-8': formatação
                json.dump(alunos, f, indent=4, ensure_ascii=False)  # mostrar as coisas que estão armazenada, indent=4: 
            print("Dados atualizados com sucesso!")
            return
            # print para mostrar alunos não cadastrado, retorna em uma variavél 
        
    print("Aluno não encontrado.") # print que o aluno não foi encntrado 

def excluir(): #Nova função para excluir 
    print("\n--- Excluir Aluno ---") #esse print é utilizado para deixar o codigo com a estetica bonita
    if not os.path.exists(BANCO_DADOS): # if:se, os.path: Verificar e montar caminhos exists: retorna False (BANCO_DADOS): arquivo
        print("Nenhum aluno cadastrado no sistema.")
        return
 # print para mostrar alunos não cadastrado, retorna em uma variavél 
    with open(BANCO_DADOS, 'r', encoding='utf-8') as f:  # arquivo no modo leitura, encoding='utf-8': formatação
        alunos = json.load(f)  #Carregar arquivo
        
    id_busca = int(input("Digite o ID do aluno que deseja remover: ")) # Variável que podemos dar valor 
    
    nova_lista = [a for a in alunos if a['id'] != id_busca] # percorre a lista e vê se o cpf ja é cadastrado
    
    if len(nova_lista) < len(alunos): # Verifica qual das lista é maior 
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f: # arquivo no modo leitura, encoding='utf-8': formatação
            json.dump(nova_lista, f, indent=4, ensure_ascii=False) # mostrar as coisas que estão armazenada, indent=4: melhoria de legibilidade  ensure_ascii=False: manter a caracteristica das palavras 
        print("Aluno removido com sucesso!") # Print para mostrar q o aluno esta removiso com sucesso 
    else:
        print("Aluno não encontrado.")
 # else : se não, para mostrar o proximo print 
def menu(): # função para mostrar menu 
    if not os.path.exists(BANCO_DADOS): 
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f: # if:se, os.path: Verificar e montar caminhos exists: retorna False (BANCO_DADOS): arquivo
            json.dump([], f) # Carregar arquivo

    while True: # Enquanto for verdadeiro 
        print("\n=== SISTEMA ESCOLAR ===") # print para deixar organizado 
        print("1. Cadastrar Aluno") # print da opcão (que seria a função 1)
        print("2. Listar Alunos") # print da opcão (que seria a função 2)
        print("3. Atualizar Aluno")  # print da opcão (que seria a função 3)
        print("4. Excluir Aluno") # print da opcão (que seria a função 4)
        print("5. Sair") # print que da a opção de sair do programa 
        
        opcao = input("Escolha uma opção: ") # input para escolher a opção desejada
        
        if opcao == '1': cadastrar() # se opção for igual a 1 executa a função 1 
        elif opcao == '2': listar() # Se opcão for igual a 2 executa a função 2
        elif opcao == '3': atualizar() # se opção for igual a 3 executa a função 3 
        elif opcao == '4': excluir() # se opção for igual a 4 executa a função 4
        elif opcao == '5': break # se aopção for igual a 5 utiliza o break para encerrar o programa 
        else: print("Opção inválida!") # se não tiver  a opção digitada mostra opção inválida 

menu() #chamando a função q mostra o menu de opções 