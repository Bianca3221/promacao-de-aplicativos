def verificar_aprovacao(nota_teste,anos_xp,possui_certificacao):
    if possui_certificacao == "sim" or (nota_teste > 80 and anos_xp >= 2):
        return True
    else:
        return False
    
nota = float(input("Digite sua nota: "))
experiancia = float(input("Digite seus anos de experiencia: "))
certificacao = input("Tem certificação?: ")

aprovado = verificar_aprovacao(nota,experiancia,certificacao)

if aprovado == True:
    print("contratar")
else:
    print("Reprovado!")