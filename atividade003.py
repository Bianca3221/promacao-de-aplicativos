temperatura = float(input("digite a temperatura atual da estufa : "))

if temperatura <= 30:
    print("clima estável")
else:
    print("ALERTA DE CALOR!")

umidade = float(input("digite a umidade atual: "))

if umidade >= 40 :
    print("Ação: ligar irrigação ativado!")
else:
    print("Ação: ligar apenas ventiladores ativado!")
        