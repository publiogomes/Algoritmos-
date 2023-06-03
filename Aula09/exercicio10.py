# Leitura da matriz
matriz = []
for i in range(2):
    linha = []
    for j in range(2):
        elemento = int(input(f"Digite o valor para a posição {i+1},{j+1}: "))
        linha.append(elemento)
    matriz.append(linha)

# Encontrar o maior elemento
maior_elemento = matriz[0][0]
for linha in matriz:
    for elemento in linha:
        if elemento > maior_elemento:
            maior_elemento = elemento

# Multiplicar a matriz pelo maior elemento
matriz_resultante = []
for linha in matriz:
    linha_resultante = []
    for elemento in linha:
        linha_resultante.append(elemento * maior_elemento)
    matriz_resultante.append(linha_resultante)

# Impressão da matriz resultante
print("Matriz resultante:")
for linha in matriz_resultante:
    print(linha)
