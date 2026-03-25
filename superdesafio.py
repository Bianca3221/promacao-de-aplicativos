livros_disponiveis = ["Python Pro","Banca de Dados", "Redes","IA","Hadware"]
livros_emprestados = []
print(f"Livros disponiveis{livros_disponiveis}")

cliente = input("Digite o nome do livro desejado: ")

if cliente in livros_disponiveis :
    indice = livros_disponiveis.index(cliente)
    livros_emprestados.append(cliente)
    livros_disponiveis.pop(indice)
    print("Emprestmo realizado com sucesso!")
    print(f"Lista atualizada: disponiveis {livros_disponiveis}, emprestados: {livros_emprestados}")
else:
    print("Desculpe esse livro não esta disponivél")

devolucão = input("digite o nome do livro para devolução: ")

if devolucão in livros_emprestados:
    indice2 = livros_emprestados.index(devolucão)
    livros_disponiveis.append(devolucão)
    livros_emprestados.pop(indice2)
    print("Devolução concluida!")
    print(f"lista atualizada: disponiveis {livros_disponiveis}, emprestados: {livros_emprestados}")
else:
    print("Esse livro não consta como emprestado")

del livros_disponiveis [0:2]
print("Relatorio final:", livros_disponiveis)