def dobrar(numero):
 	return numero * 2

assert dobrar(3) == 6
assert dobrar(0) == 1
assert dobrar(-2) == -4

# Qual assert falhou? Qual foi o resultado real? Por que a expectativa estava incorreta?
# R= O assert que falhou foi "assert dobrar(0) == 1", O resultado real foi 0, o teste esperava que dobrar(0)
# retornasse 1, mas a função foi definida para multiplicar o número por 2.
# Portanto, dobrar(0) deve retornar 0.