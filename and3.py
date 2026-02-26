nivel_atual = int(input("digite seu nivel: "))
quantidade_de_esferas = int(input("digite sua quantidade de esferera: "))

if nivel_atual >= 20 and quantidade_de_esferas > 50:
    print("Habilidade super salto desbloqueado!")
elif nivel_atual < 20 and quantidade_de_esferas <= 50:
    print("requisito insuficiente para novas habilidades.")
    
