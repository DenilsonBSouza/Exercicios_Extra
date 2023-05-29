def verificar_palindromo(string):
    string = string.lower()  
    string = string.replace(" ", "") 

    if string == string[::-1]:
        return True
    else:
        return False

texto1 = "arara"
texto2 = "ovo"
texto3 = "python"

print("Texto 1 é palíndromo?", verificar_palindromo(texto1))
print("Texto 2 é palíndromo?", verificar_palindromo(texto2))
print("Texto 3 é palíndromo?", verificar_palindromo(texto3))
