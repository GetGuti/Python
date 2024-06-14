
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Erro: Divisão por zero"


def calculadora():
    while True:
        print("Escolha a operação:")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Sair")

        escolha = input("Digite sua escolha (1/2/3/4/5): ")

        if escolha == '5':
            print("Saindo...")
            break

        while escolha not in ['1', '2', '3', '4']:
            print("Opção inválida. Por favor, escolha uma opção válida (1/2/3/4/5).")
            escolha = input("Digite sua escolha (1/2/3/4/5): ")


        try:
            num1 = input("Digite o primeiro número: ")
            while not num1.isnumeric():
                print("Erro: Entrada inválida. Certifique-se de digitar um número válido.")
                num1 = input("Digite o primeiro número: ")
            num1 = float(num1)

            num2 = input("Digite o segundo número: ")
            while not num2.isnumeric():
                print("Erro: Entrada inválida. Certifique-se de digitar um número válido.")
                num2 = input("Digite o segundo número: ")
            num2 = float(num2)
        except ValueError:
            print("Erro: Entrada inválida. Certifique-se de digitar um número válido.")
            return

        if escolha == '1':
            print(f"{num1} + {num2} = {soma(num1, num2)}")
        elif escolha == '2':
            print(f"{num1} - {num2} = {subtracao(num1, num2)}")
        elif escolha == '3':
            print(f"{num1} * {num2} = {multiplicacao(num1, num2)}")
        elif escolha == '4':
            if num2 == 0:
                print("Erro: Divisão por zero não é permitida.")
            else:
                print(f"{num1} / {num2} = {divisao(num1, num2)}")


calculadora()