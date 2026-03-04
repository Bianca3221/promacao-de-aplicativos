valor_da_compra = int(input("digite o valor da compra: "))
cliente = input("Você é prime?: ")
frete = 50.00

if valor_da_compra >= 500.00 or (cliente == "sim" and valor >= 100.00) :
    print("frete grátis! ")
    frete = 00.00
    print("valor total da compra:", valor_da_compra)
valor_da_compra = valor_da_compra + frete
print("valor total da compra: ", valor_da_compra)



