def calc_par_impar():
    contador_par = 0
    contador_impar = 0
    
    for i in range(10):
        numero = int(input(f"Digite o {i+1}º número: "))
        if numero % 2 == 0:
            contador_impar += 1
        else:
            contador_par += 1
    
    return contador_impar, contador_par

par, impar = calc_par_impar()

print(f"A qunatidade de números pares é: {par}")
print(f"A qunatidade de números impares é: {impar}")