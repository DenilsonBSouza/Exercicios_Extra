def calc_soma_media():
    soma = 0
    
    for i in range(5):
        numero = float(input(f"Digite o {i+1}º número: "))
        soma  += numero
        
    media = soma / 5
    return soma, media

soma, media = calc_soma_media()

print(f"A soma dos números é: {soma:,.2f}")
print(f"A media dos números é: {media:,.2f}")