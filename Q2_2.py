salario = float(input("Digite o seu salário base em R$: "))

if salario < 1903.98:
    print("Isento")
    
elif salario > 1903.99 and salario < 2526.65:
    imp_renda = (salario * 0.075) - 142.80
    print(f'O valor do imposto de renda é R$ {imp_renda:,.2f} reais') 
    
elif salario > 2628.66 and salario < 3751.05:
    imp_renda = (salario * 0.15) - 354.80
    print(f'O valor do imposto de renda é R$ {imp_renda:,.2f} reais')
    
elif salario > 3751.06 and salario < 4664.68:
    imp_renda = (salario * 0.225) - 636.13
    print(f'O valor do imposto de renda é R$ {imp_renda:,.2f} reais')
    
else:
    salario > 4664.69
    imp_renda = (salario * 0.275) - 869.36 
    print(f'O valor do imposto de renda é R$ {imp_renda:,.2f} reais')
        
