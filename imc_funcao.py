nome_usuario = input("Digite o nome de usario: ")
peso_usuario = int(input("Digite seu peso: "))
altura_usuario = int(input("Digite sua altura: "))
categoria_usuario = ""

def geral_relatorio_saude(nome,peso,altura,idade,categoria):
    imc = peso / (altura ** 2)
    if imc <= 18.5:
        categoria = "Baixo peso"
    elif imc > 18.5 and imc <24.9:
        categoria = "peso normal"
    elif imc >18.5 and imc < 24.9: 
        categoria = "Sobrepeso"
    elif imc >= 29.9:
        categoria = "OBESSIDADE"
    print(f"OLá {nome}, idade: {idade}, seu imc: {categoria}")