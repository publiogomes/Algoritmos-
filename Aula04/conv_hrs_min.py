hora = float(input("Digite as horas (HH.MM): "))

horas = int(hora)
minutos = int((hora - horas) * 60)

total_minutos = horas * 60 + minutos

print("A hora digitada equivale a", total_minutos, "minutos.")
