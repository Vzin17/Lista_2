nota = float(input("Digite uma nota:"))
nota2 = float(input("Digite a segunda nota: "))
media = (nota + nota2) /2

if media >= 0 and media <= 10:
    print(f"A media sera de: {media}")
else:
    print("O valor eh invalido!!")
