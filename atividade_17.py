def soma(a, b):
    return a + b
def menos(a, b):
    return a - b
def multi(a, b):
    return a * b
def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "ERRO: Divisao por zero"

def menu():
    print("Menu de operacoes!")
    print("""
          1. Soma
          2. Menos
          3. Multiplicaçao
          4. Divisao
          """)

def main():
    menu()
    escolha = input("Escolha uma operaçao [1/2/3/4]")
    
    if escolha in ['1', '2', '3', '4']:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if escolha == '1':
            print("Resultado:", soma(num1, num2))
        elif escolha == '2':
            print("Resultado:", menos(num1, num2))
        elif escolha == '3':
            print("Resultado:", multi(num1, num2))
        elif escolha == '4':
            print("Resultado:", divisao(num1, num2))
    else:
        print("Opção inválida!")


if __name__ == "__main__":
    main()