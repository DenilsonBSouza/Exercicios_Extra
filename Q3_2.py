def obter_maior_num():
    maior_numero = int(input("Digite o primeiro número: "))
    
    for i in range(1,5):
        numero = int(input(f"Digite o {i+1}º número: "))
        if numero > maior_numero:
            maior_numero = numero
    return numero

maior_num = obter_maior_num()

print(f"O maior número é: {maior_num}")
