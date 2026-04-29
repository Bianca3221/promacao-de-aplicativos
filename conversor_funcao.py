def converter_km_para_ms(velocidade_km): 
    if velocidade_km> 80:
        velocidade_ms = velocidade_km / 3.6
        print(f"A velociade convertida: {velocidade_ms}")
        print("Rduza a velocidade! ")
    else:
        print("Velocidade normal ")
    velocidade = int(input("Qual a velocidade atual? : "))
    converter_km_para_ms(velocidade)