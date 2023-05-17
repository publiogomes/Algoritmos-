altura_degrau_cm = float(input("Digite a altura do degrau em centímetros: "))
altura_objetivo_m = float(input("Digite a altura que deseja alcançar em metros: "))

altura_degrau_m = altura_degrau_cm / 100 # Conversão de centímetros para metros
numero_degraus = altura_objetivo_m / altura_degrau_m

print("Número de degraus a subir:", int(numero_degraus))