def ordenar_vetor(vetor):
    n = len(vetor)
    for i in range(n):
        for j in range(0, n-i-1):
            if vetor[j] > vetor[j+1]:
                vetor[j], vetor[j+1] = vetor[j+1], vetor[j]

# Lendo os números inteiros e armazenando no vetor A
A = []
for i in range(10):
    numero = int(input(f"Digite o número {i+1}: "))
    A.append(numero)

# Ordenando o vetor A
ordenar_vetor(A)

# Copiando o vetor A para o vetor B
B = A.copy()

# Mostrando os vetores A e B
print("Vetor A:", A)
print("Vetor B:", B)
