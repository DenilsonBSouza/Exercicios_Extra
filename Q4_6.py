def calcular_tempo_total(dias, horas, minutos, segundos):
    total_segundos = segundos
    total_segundos += minutos * 60
    total_segundos += horas * 60 * 60
    total_segundos += dias * 24 * 60 * 60
    return total_segundos

tempo_total = calcular_tempo_total(2, 5, 10, 30)
print(tempo_total)
