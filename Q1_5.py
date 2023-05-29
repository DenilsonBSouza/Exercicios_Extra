import math

area_pintada = float(input("Informe em metros quadrados a área a ser pintada: "))

rend_latas = math.ceil (area_pintada / 3)
qtd_lata = math.ceil (rend_latas / 18)
preco_total = qtd_lata * 80.00

print(f'Quantidade latas de tintas a ser comprada: {qtd_lata:,.2f}')
print(f'Preço total é R$: {preco_total:,.2f}')