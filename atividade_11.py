import math
numero = int(input("Digite um numero: "))

if numero < 0:
    print("Numero invalido")
else:
    logaritmo = math.log(numero)
    print(f"O logaritmo de {numero} eh: {logaritmo}")
