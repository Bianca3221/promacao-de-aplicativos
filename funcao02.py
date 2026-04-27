def senha_valida (senha):
    tentativas = input("Digite sua senha: ")

    if len(senha)<6 :
        print("Senha invalida!")
        tentativas = input("Digite a senha novamente: ")
    elif len(senha)>=6 : 
        