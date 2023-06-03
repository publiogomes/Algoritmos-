# Leitura da matriz
matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        elemento = float(input(f"Digite o valor para a posição {i+1},{j+1}: "))
        linha.append(elemento)
    matriz.append(linha)

# Criação da matriz transposta
matriz_transposta = []
for j in range(3):
    linha_transposta = []
    for i in range(3):
        linha_transposta.append(matriz[i][j])
    matriz_transposta.append(linha_transposta)

# Impressão da matriz transposta
print("Matriz transposta:")
for linha in matriz_transposta:
    print(linha)
