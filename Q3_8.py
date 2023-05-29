def gerar_triangulo(n):
    for i in range(1, n+1):
        linha = "*" * i
        print(linha)

tamanho = int(input("Digite o tamanho do triângulo: "))

gerar_triangulo(tamanho)
