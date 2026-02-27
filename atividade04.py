temperatura = float(input("Digite a temperatura: "))

if temperatura >= 80 :
    print("PERIGO! desligando servidor por superaquecimento! ")
elif temperatura >= 50 :
    print("ALERTA! ventoinhas ligadas no maximo")
elif temperatura < 50 :
    print("Temperatura estavel. Sistema operando normalmente.")
    

