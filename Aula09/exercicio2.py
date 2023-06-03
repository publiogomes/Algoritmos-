def encontrar_maior_valor(vetor):
    maior = vetor[0]
    posicao = 0

    for i in range(1, len(vetor)):
        if vetor[i] > maior:
            maior = vetor[i]
            posicao = i

    return maior, posicao


# Carregando o vetor
vetor = []
for i in range(10):
    elemento = int(input("Digite o elemento {}: ".format(i + 1)))
    vetor.append(elemento)

# Encontrando o maior valor e sua posição
maior_valor, posicao = encontrar_maior_valor(vetor)

# Imprimindo o resultado
print("O maior valor é", maior_valor)
print("Sua posição no vetor é", posicao)
