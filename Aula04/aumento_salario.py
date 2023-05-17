salario = float(input("Digite o salário do funcionário: "))
percentual_aumento = float(input("Digite o percentual de aumento (%): "))

valor_aumento = salario * (percentual_aumento / 100)
novo_salario = salario + valor_aumento

print("O valor do aumento é:", valor_aumento)
print("O novo salário é:", novo_salario)
