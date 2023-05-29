def testar_primo(numero):
    if numero < 2:
        return False

    divisores = []
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            divisores.append(i)

    return divisores


numero = int(input("Digite um número inteiro: "))

divisores = testar_primo(numero)

if divisores:
    print(f"{numero} não é um número primo. É divisível por:")
    for divisor in divisores:
        print(divisor)
else:
    print(f"{numero} é um número primo.")
