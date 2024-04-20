salario = float(input("Digite o salario aqui: "))
emprestimo = float(input("Digite o valor do emprestimo: "))
porcentagem_S = salario * 0.20


if salario < porcentagem_S:
    print("EMPRESTIMO RECUSADO!")
elif emprestimo > porcentagem_S:
    print("RECUSADO")
else:
    print("EMPRESTIMO ACEITO!")
