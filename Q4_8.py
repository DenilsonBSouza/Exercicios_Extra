def calcular_mdc(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def main():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    mdc = calcular_mdc(num1, num2)

    print("O MDC de", num1, "e", num2, "é:", mdc)

if __name__ == '__main__':
    main()
