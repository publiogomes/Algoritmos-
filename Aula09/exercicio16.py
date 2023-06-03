# Leitura da matriz
matriz = []
for i in range(5):
    linha = []
    for j in range(5):
        elemento = float(input(f"Digite o valor para a posição {i+1},{j+1}: "))
        linha.append(elemento)
    matriz.append(linha)

# Cálculo da média das linhas pares
soma_linhas_pares = 0
contador_linhas_pares = 0
for i in range(1, 5, 2):
    soma_linhas_pares += sum(matriz[i])
    contador_linhas_pares += 5

media_linhas_pares = soma_linhas_pares / contador_linhas_pares

# Impressão da média das linhas pares
print(f"A média dos elementos nas linhas pares da matriz é: {media_linhas_pares}")
