def avaliar_desempenho (nota):

    if nota >=9:
        return "EXECELENTE!"
    elif nota >=7:
        return "BOM"
    elif nota > 5 :
        return "regular!"
    else:
        return "insuficiente"
    
    nota_usuario = int(input("Digite sua nota : "))
    mensagem = avaliar_desempenho(nota_usuario)
    print(mensagem)