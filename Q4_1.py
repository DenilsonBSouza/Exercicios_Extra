def calcular_potencia(base, expoente):
    resultado = 1

    for _ in range(expoente):
        resultado *= base

    return resultado


base = float(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))

potencia = calcular_potencia(base, expoente)
print(f"O resultado da potência de {base} elevado a {expoente} é: {potencia}")
