def contar_vogais(s):
    vogais = 'aeiouAEIOU'  
    count = 0  
    
    for char in s:
        if char in vogais:
            count += 1
    
    return count

resultado = contar_vogais("Alemanha")
print(resultado)
