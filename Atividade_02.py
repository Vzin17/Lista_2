import math
Numero = float(input("Digite um numero: "))
if (Numero >= 0):
    Raiz = math.sqrt(Numero)
    print(f"A raiz quadrada de {Numero} eh: {Raiz}")
else:
    print("Esse numero eh invalido")
