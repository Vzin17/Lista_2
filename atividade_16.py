base_maior = float(input("Digite a base maior: "))
base_menor = float(input("Digite a bese menor: "))
altura  = float(input("Digite a altura do trapezio: "))

if base_maior <= 0 and base_menor <= 0:
    print("INVALIDO")
else:
    print("Verifique a area abaixo!")
    area = (base_maior+base_menor+altura) /2
    print(f"A area do trapezio eh de: {area}")

