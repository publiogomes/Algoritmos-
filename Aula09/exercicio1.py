vetor = []
for i in range(5):
    x = int(input(f"Digite o {i+1}o. valor: "))
    vetor.append(x)
for i in range(4, -1, -1):
    print(vetor[i], end='')
    print(vetor[::-1], end='/n')
    vetor.reverse()

