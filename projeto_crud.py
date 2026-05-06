estoque = []
acao = 0

# adiciona o item dentro da lista 
def adicionar_lista (nome,estoque):
    estoque.append(nome)

# vai listar o produto desejado
def listar_produtos(estoque):
    for nome in estoque:
        indice = estoque.index(nome)
        print(f"posição: {indice}, Nome: {nome}")
        
# Substituir o produto pelo o outro que deseja 
def atualizar_produto(indice,novo_nome,estoque):
    estoque[indice] = novo_nome

def remover_produto(indice):
    remover = estoque.pop(indice)
    print(f"item {remover} removido!")

# mostra as opções q existem dentro do menu para executar as funções 
def exibir_menu(acao):
    while acao != 5:
        print("PROGRAMA INICIANDO")
        print("1- Adicionar produto")
        print("2- Listar produto")
        print("3- Atualizar produto")
        print("4- Remover produto da lista ")
        print("5- Sair")

        acao = int(input("Digite a ação desejada: "))

        if acao == 1 :
            produto = input("Digite o nome do produto: ")
            adicionar_lista(produto,estoque)

        elif acao == 2 :
            listar_produtos(estoque)
        
        elif acao == 3 :
            atualizar = input("Digite o nome do produto que deseja atualizar: ")
            indice = estoque.index(atualizar)
            nome_novo = input("Digite o nome do novo produto: ")
            atualizar_produto(indice,nome_novo,estoque)

        elif acao == 4 :
            remover = input("Digite o nome do produto que deseja remover: ")
            indice = estoque.index(remover)
            remover_produto(indice)
       
        elif acao == 5 :
            print("Programa encerrado!")
            return

exibir_menu(acao)