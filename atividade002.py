curso = input("você tem o curso de segurança completo S/N: ")

if curso == "S":
    pergunta = input("O instrutor está presente na sala?: ")
    if pergunta == "S":
        print ("acesso liberao: operação iniciada")
    else:
        print ("aguarde o instrutor para ligar a máquina")

else:
    print("acesso negado: faça o treinamento")


