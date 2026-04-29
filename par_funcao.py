def eh_par(numero) :
    if numero %2 == 0:
        return True
    else:
        return False
    
numero_usuario = int(input("Digite seu numero: "))

msg = eh_par(numero_usuario) 
print(msg)