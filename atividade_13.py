nota1 = float(input("Digite a notado trabalho: "))
nota2 = float(input("Digite a nota semestral: "))
nota3 = float(input("Digite a nota do exame final: "))
media_aluno = (nota1 + nota2 + nota3) /3

if media_aluno >= 0 and media_aluno <= 2.9:
    print("REPROVADO")
elif media_aluno >= 3 and media_aluno <= 4.9:
    print("RECUPERAÇAO")
else:
    print("APROVADO")
