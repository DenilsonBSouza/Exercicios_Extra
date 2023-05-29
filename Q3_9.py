def armazenar_notas():
    conceito_a = []
    conceito_b = []
    conceito_c = []
    conceito_d = []
    conceito_e = []

    while True:
        nota = float(input("Digite uma nota (-1 para sair): "))
        if nota == -1:
            break
        elif 9.0 <= nota <= 10.0:
            conceito_a.append(nota)
        elif 8.0 <= nota < 9.0:
            conceito_b.append(nota)
        elif 7.0 <= nota < 8.0:
            conceito_c.append(nota)
        elif 6.0 <= nota < 7.0:
            conceito_d.append(nota)
        elif 0.0 <= nota < 6.0:
            conceito_e.append(nota)
        else:
            print("Nota inválida. Digite um valor entre 0 e 10.\n")

    return conceito_a, conceito_b, conceito_c, conceito_d, conceito_e

conceito_a, conceito_b, conceito_c, conceito_d, conceito_e = armazenar_notas()

print("Conceito A:", conceito_a)
print("Conceito B:", conceito_b)
print("Conceito C:", conceito_c)
print("Conceito D:", conceito_d)
print("Conceito E:", conceito_e)
