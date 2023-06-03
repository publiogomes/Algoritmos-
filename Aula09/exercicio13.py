# Leitura da matriz
matriz = []
for i in range(10):
    linha = []
    for j in range(10):
        elemento = int(input(f"Digite o valor para a posição {i+1},{j+1}: "))
        linha.append(elemento)
    matriz.append(linha)

# Encontrar a posição do maior elemento
maior_elemento = matriz[0][0]
linha_maior = 0
coluna_maior = 0
for i in range(10):
    for j in range(10):
        if matriz[i][j] > maior_elemento:
            maior_elemento = matriz[i][j]
            linha_maior = i
            coluna_maior = j

# Impressão da posição do maior elemento
print(f"A posição do maior elemento ({maior_elemento}) é: ({linha_maior+1},{coluna_maior+1})")
