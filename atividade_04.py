import math
Numero = float(input("Digite um numero: "))

if Numero >= 0:
    Raiz = math.sqrt(Numero)
    print(f"{Numero**2} e a raiz eh {Raiz}")
else:
    print("Numeor invalido!!")
