def valores(a, b, c):
    if a == b and a == c:
        print("Temos um triangulo Equilatero")
    elif b == c and b != a:
        print("Isso eh um triangulo Isoceles")
    elif a != b and a != c and b != c:
        print("Isso eh um triangulo Escaleno")
    else:
        print("Isso nao eh um triangulo")

num1 = float(input("Digite um numero: "))
num2 = float(input("Digite outro numero: "))
num3 = float(input("Digite outro numero: "))
if valores(num1, num2, num3):
    print("O triangulo eh Equilatero", valores(num1, num2, num3))
    print("O triangulo eh Isoceles", valores(num1, num2, num3))
    print("O triangulo eh Escaleno", valores(num1, num2, num3))
else:
    print("INVALIDO")


