val_hora = float(input("Informe o seu ganho por hora em R$: "))
hora_trabalhada = float(input("Informe as horas trabalhadas: "))    

sal_bruto = val_hora * hora_trabalhada
inss = sal_bruto * 0.10
sind = sal_bruto * 0.02
desc_renda = sal_bruto * 0.15
sal_liq = sal_bruto - inss - sind - desc_renda 

print(f'Valor pago ao INSS no mês em R$: {inss:,.2f}') 
print(f'Descontos sindical R$: {sind:,.2f}')
print(f'O salário bruto é R$: {sal_bruto:,.2f}')
print(f'Salário líquido R$: {sal_liq:,.2f}')
