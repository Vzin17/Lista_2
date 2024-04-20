ano = float(input("Informe algum ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("Sim ele eh bissexto")
else:
    print("Nao eh bissexto")
