def classificar_temperatura(temperatura):
    if temperatura < 15:
        return "Frio"
    elif temperatura <= 25:
        return "Agradável"
    else:
        return "Quente"



assert classificar_temperatura(10) == "Frio"
assert classificar_temperatura(14) == "Frio"
assert classificar_temperatura(15) == "Agradável" 
assert classificar_temperatura(20) == "Agradável"
assert classificar_temperatura(25) == "Agradável"   
assert classificar_temperatura(26) == "Quente"
assert classificar_temperatura(30) == "Quente"

# “Eu testei a temperatura 15, que é um dos limites pedidos. Como a regra diz que de 15 até 25 graus a temperatura é ‘Agradável’,
# o resultado esperado é Agradável. Por isso usei assert classificar_temperatura(15) == "Agradável".”