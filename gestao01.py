id = int(input("Qual o seu id ? :"))
temperatura = float(input("qual a temperatura? :"))
tempo_uso = int(input("Qual tempo de uso ? :"))

if (id % 3 == 0 ) and (temperatura > 40 or tempo_uso > 8):
    print(f"funcionario {id}, você foi escalado para a manutenção preventiva hoje.")
else:
    print(f"funcionario {id}, sua maquina opera dentro dos padrões normais.")
    