def obter_numeros_positivos(lista):
    numeros_positivos = []

    for numero in lista:
        if numero > 0:
            numeros_positivos.append(numero)

    return numeros_positivos


lista_original = [1, -2, 3, -4, 5, -6, 7, -8, 9]
sub_lista_positivos = obter_numeros_positivos(lista_original)

print("Lista original:", lista_original)
print("Sub-lista de números positivos:", sub_lista_positivos)
