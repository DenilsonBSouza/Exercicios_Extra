notas_disponiveis = [10, 50, 100, 200]

valor_saque = int(input("Digite o valor do saque: "))

if valor_saque < 10 or valor_saque > 1000:
    print("Valor de saque inválido. O valor deve ser entre 10 e 1000.")
else:
    quantidade_notas = {}
    for nota in notas_disponiveis:
        if valor_saque >= nota:
            quantidade = valor_saque / nota
            quantidade_notas[nota] = quantidade
            valor_saque -= quantidade * nota

    print("Quantidade de notas fornecidas:")
    for nota, quantidade in quantidade_notas.items():
        if quantidade > 0:
            print(f"Notas de {nota} reais: {quantidade}")
