def gerar_quadrado(n):
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()

tamanho = int(input("Digite o tamanho do quadrado: "))

gerar_quadrado(tamanho)
