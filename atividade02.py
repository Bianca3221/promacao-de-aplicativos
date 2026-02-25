nome_do_heroi = input("digite o nome do seu heroi: ")
nome_do_ataque = float(input("seu poder: "))
ponto_de_defesa =float (input("sua defesa: "))

dano = nome_do_ataque - ponto_de_defesa 
  
if dano <= 0 :
    print("O vilão bloqueou o ataque! dano = 0")
elif dano > 0 :
    print("ataque critico! Você causou dano ao vilão", [dano])

    
    