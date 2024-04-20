idade = float(input("Digite sua idade em anos: "))
Tempo_Trab = float(input("Digite quantos anos esse trabalhador tem: "))

if idade >= 65:
    print("Pode se aposentar!")
elif Tempo_Trab >= 30:
    print("Pode se aposentar!")
elif idade == 60 and Tempo_Trab == 25:
    print("Pode se aposentar tambem!")
else:
    print("Infelizmente nao sera possivel requerer o ato de ficar isento de trabalho")
