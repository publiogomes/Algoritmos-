palavras = []

# Leitura das palavras
for _ in range(20):
    palavra = input("Digite uma palavra de no máximo 10 caracteres: ")
    palavras.append(palavra)

# Processamento das palavras
palavras_invertidas = []
for palavra in palavras:
    palavra_invertida = palavra[::-1]  # Inverte os caracteres da palavra
    palavras_invertidas.append(palavra_invertida)

# Exibição das palavras invertidas
print("Palavras invertidas:")
for palavra in palavras_invertidas:
    print(palavra)
