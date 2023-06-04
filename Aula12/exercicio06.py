def converter_para_segundos(horas, minutos, segundos):
    total_segundos = horas * 3600 + minutos * 60 + segundos
    return total_segundos

'''segundos_total = converter_para_segundos(2, 40, 10)
print(segundos_total)'''

n = int(input("Digite o horário: "))
segundos_total = converter_para_segundos()
resultado = converter_para_segundos(n)
print(segundos_total)