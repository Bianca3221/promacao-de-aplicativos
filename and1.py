idade = float(input("digite sua idade: "))
saldo = float(input("digite seu saldo: "))

if idade >= 18 and saldo >= 50.00 :
    print ("Acesso autorizado, Bem vindo ao evento")
elif idade < 18 and saldo < 50.00:
    print ("infelizmente você nao cumpre os requisito de entrada.")
