senha_correta= "123B"
senha = input("Digite sua senha: ")
tentativas = 0

while senha != senha_correta and tentativas < 2:
    senha = input("Digite a senha novamente!: ")
    tentativas += 1 

if tentativas == 2 :
    print("Acesso bloqueado!")

else:
    print("SEJA BEM VINDO!!!")