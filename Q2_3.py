A = 'alcool'
G = 'gasolina' 
    
litros_vendidos = float(input("Digite o número de litros de combustíveis vendidos: "))
tipo_combustivel = str(input("Digite o tipo de coms=bustível vendido: "))

if tipo_combustivel == A:
    if litros_vendidos < 20.0:
        valor_combustivel = (litros_vendidos * 2.80) * 0.003
        print(f'O valor total a ser pago é R$ {valor_combustivel:,.2f} reais')
else:
    valor_combustivel = (litros_vendidos * 2.80) * 0.005
    print(f'O valor total a ser pago é R$ {valor_combustivel:,.2f} reais')