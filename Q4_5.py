def contar_ocorrencias(s, c):
    contador = 0

    for caractere in s:
        if caractere == c:
            contador += 1

    return contador

# Exemplo de uso da função
texto = "laranjamecanica"
caractere = "a"

ocorrencias = contar_ocorrencias(texto, caractere)
print("Número de ocorrências:", ocorrencias)
