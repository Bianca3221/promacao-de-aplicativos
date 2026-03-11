codigo = int(input("digite seu codigo: "))
peso = float(input("qual o kg do seu pacote?: "))
status = "entrega normal"

if peso > 50 :
    print("carga pesada")
elif peso < 5 and codigo % 10 == 0 :
    print("entrega expressa!")
else:
    status: "entrega padrão"
print (f"pacote {codigo}: peso ")

