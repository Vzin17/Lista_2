
def divisivel_por_3_ou_5(numero):
    if numero % 3 == 0 and numero % 5 != 0:
        return True
    elif numero % 5 == 0 and numero % 3 != 0:
        return True
    else:
        return False

numero = int(input("Digite um numero: "))
if divisivel_por_3_ou_5(numero):
    print(numero, "O numero eh divisivel por 3 ou 5, mas nao pelos dois!")
else:
    print(numero, "Nao eh divisivel por 3 ou 5, ou eh divisivel pelos 2 simultaneamente!")
