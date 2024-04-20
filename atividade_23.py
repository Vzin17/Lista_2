idade = int(input("Digite a idade aqui: "))

if idade == 5 or idade <= 7:
    print("Esta na categoria Infantil A!")
elif idade == 8 or idade <= 10:
    print("Esta na categoria Infantil B!")
elif idade == 11 or idade <= 13:
    print("Esta na categoria Juvenil A!")
elif idade == 14 or idade <= 17:
    print("Esta na categoria Juvenil B!")
elif idade >= 18:
    print("Esta na categoria Senior!")
