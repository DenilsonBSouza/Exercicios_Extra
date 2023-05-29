tam_arq = int(input("Informe o tamanho do arquivo: "))
vel_net = int(input("Informe a velocidade da internet: "))

tempo_download = (tam_arq * 8) / vel_net / 60

print(f'O tempo aproximado para fazer o download é {tempo_download:,.2f} minutos')