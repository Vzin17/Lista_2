import math
dia = int(input("Digite um numero de 1 à 7: "))

if (dia > 7) or (dia <= 0):
    print("Numero invalido!")
else:
    print("Numero valido, abaixo o dia da semana correspondente!")

match dia:
    case 0:
        print("INVALIDO")
    case 1:
        print("Domingo")
    case 2:
        print("Segunda-feira")
    case 3:
        print("Terça-feira")
    case 4:
        print("Quarta-feira")
    case 5:
        print("Quinta-feira")
    case 6:
        print("Sexta-feira")
    case 7:
        print("Sabado")
    case 0:
        print("INVALIDO")
