# Função para carregar o dicionário
def carregar_dicionario():
    dicionario = {}
    total_idades = 0
    num_pares = int(input("Digite o número de pares (nome, idade): "))
    for i in range(num_pares):
        nome = input(f"Digite o nome da pessoa {i+1}: ")
        idade = int(input(f"Digite a idade da pessoa {i+1}: "))
        dicionario[nome] = idade
        total_idades += idade
    return dicionario, total_idades

# Função para encontrar os nomes com idade maior que a média
def encontrar_nomes_maior_media(dicionario, total_idades):
    media = total_idades / len(dicionario)
    nomes_maior_media = []
    for nome, idade in dicionario.items():
        if idade > media:
            nomes_maior_media.append(nome)
    return nomes_maior_media

# Carregar o dicionário
dicionario, total_idades = carregar_dicionario()

# Encontrar os nomes com idade maior que a média
nomes_maior_media = encontrar_nomes_maior_media(dicionario, total_idades)

# Mostrar os nomes com idade maior que a média
print("Nomes com idade maior que a média:")
for nome in nomes_maior_media:
    print(nome)
