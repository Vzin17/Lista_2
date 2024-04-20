import math
Numero = float(input("Digite um numero: "))
if Numero >= 0:
    Raiz = math.sqrt(Numero)
    print(f"A raiz eh: {Numero}")
else:
    print(f"{Numero**2}")
