cargo = input("coloque seu cargo: ")
codigo = int(input("digite seu codigo: "))
botao_de_emergenci = input("botão de emergencia pressionado?:")
epi = input("EPI completo?: ")

if (cargo == "engenheiro" or cargo =="tecnico") and (codigo == 1234 or botao_de_emergencia == "sim") and epi == "sim":
    print("sistema liberado!")
else:
    print("ACESSO NEGADO, risco de segurança")


