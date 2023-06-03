# Leitura da matriz
matriz = []
for i in range(4):
    linha = []
    for j in range(4):
        elemento = float(input(f"Digite o valor para a posição {i+1},{j+1}: "))
        linha.append(elemento)
    matriz.append(linha)

# Cálculo da soma da diagonal principal
soma_diagonal = 0
for i in range(4):
    soma_diagonal += matriz[i][i]

# Impressão da soma da diagonal principal
print(f"A soma dos elementos da diagonal principal é: {soma_diagonal}")
