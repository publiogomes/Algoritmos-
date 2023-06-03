# Inicialização dos vetores
vetor1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
vetor2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Criação do terceiro vetor
vetor3 = []

# Intercalação dos vetores
for i in range(len(vetor1)):
    vetor3.append(vetor1[i])
    vetor3.append(vetor2[i])

# Impressão do vetor resultante
print(vetor3)

