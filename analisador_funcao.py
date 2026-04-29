def contar_caracteres(palavra):
    if len (palavra)<5:
        print("Nome curto, minimo 5 caracteres! ")
    else :
        print("Nome cadastrado!  ")
    nome = input("Digite seu nome para o acesso: ")
    contar_caracteres(nome)