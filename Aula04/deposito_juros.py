deposito = float(input("Digite o valor do depósito: "))
juros = float(input("Digite a taxa de juros (0.0): "))

rendimento = deposito * juros
val_tot = deposito + rendimento

print("O valor do rendimento é:", rendimento)
print("O valor total após o rendimento é:", val_tot)
