while True:
    print("\n=== CALCULADORA ===")

    num1 = float(input("Digite o primeiro número: "))
    operacao = input("Digite a operação (+, -, *, /): ")
    num2 = float(input("Digite o segundo número: "))

    if operacao == "+":
        resultado = num1 + num2
    elif operacao == "-":
        resultado = num1 - num2
    elif operacao == "*":
        resultado = num1 * num2
    elif operacao == "/":
        if num2 == 0:
            print("Erro: não é possível dividir por zero.")
            continue
        resultado = num1 / num2
    else:
        print("Operação inválida.")
        continue

    print("Resultado:", resultado)

    continuar = input("Deseja realizar outro cálculo? (s/n): ")

    if continuar.lower() != "s":
        print("Calculadora encerrada.")
        break
