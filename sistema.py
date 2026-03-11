senha = input("Digite sua senha: ")
tentativa = float(input("digite o numero de tentativas "))
token = input ("digite seu token: ")
 
if (senha == "admin1234" ) and (tentativa % 3 == 0 or token == "vip"):
    print(f"tentativa {tentativa} ACESSO LIBERADO!")
else :
    print(f"tentativa {tentativa} ACESSO BLOQUEADO POR PROTOCOLO!")

