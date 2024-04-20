nota = float(input("Digite a nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))
nota2 = nota2*2
media_nota = nota + nota2 /3
media = 7

if media_nota <= media:
    print("REPROVADO")
else:
    print("APROVADO")
