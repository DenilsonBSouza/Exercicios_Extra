peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

imc = peso / altura

if imc >= 18.5 and imc < 25.0:
    print("Peso normal")
elif imc > 25.5:
    print("Sobrepeso")
else:
    imc < 18.5
    print("Abaixo do peso")    
    
