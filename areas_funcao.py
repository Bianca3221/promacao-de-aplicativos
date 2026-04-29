tentativas_usuario = 0 
largura_area = int(input("Digite a largura: "))
comprimento_area = int(input("Digite o comprimento: "))

def calcular_area(largura, comprimento, tentativas):
    while tentativas != 3:
        multiplicacao = largura * comprimento 
        print(f"area calculada: {multiplicacao}")
        largura = int(input("Digite a largura: "))
        comprimento = int(input("Digite o comprimento: "))
        tentativas += 1     
    
    calcular_area(largura_area, comprimento_area,tentativas_usuario )

