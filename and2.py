media_final = float(input("digite sua media final: "))
porcentagem_de_presenca = int(input("digite sua porcentagem de presença: "))

if media_final >= 7.0 and porcentagem_de_presenca >= 75:
    print("Parabéns!, Você foi aprovado")
elif media_final < 70 and porcentagem_de_presenca < 75 :
    print("Reprovado!, verifique sua nota ou presença!")
    
