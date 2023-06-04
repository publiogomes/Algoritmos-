# Função para carregar o dicionário
def carregar_dicionario():
    dicionario = {}
    for i in range(10):
        sobrenome = input(f"Digite o sobrenome da pessoa {i+1}: ")
        idade = int(input(f"Digite a idade da pessoa {i+1}: "))
        dicionario[sobrenome] = idade
    return dicionario

# Função para encontrar o sobrenome da pessoa mais velha
def encontrar_pessoa_mais_velha(dicionario):
    pessoa_mais_velha = max(dicionario, key=dicionario.get)
    return pessoa_mais_velha

# Carregar o dicionário
dicionario = carregar_dicionario()

# Encontrar o sobrenome da pessoa mais velha
pessoa_mais_velha = encontrar_pessoa_mais_velha(dicionario)

# Escrever o sobrenome da pessoa mais velha
print("Sobrenome da pessoa mais velha:", pessoa_mais_velha)
