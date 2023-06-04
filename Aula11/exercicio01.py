# Função para carregar a tupla
def carregar_tupla():
    tupla = ()
    for i in range(10):
        elemento = int(input(f"Digite o elemento {i+1}: "))
        tupla += (elemento,)
    return tupla

# Função para escrever a tupla na ordem inversa
def escrever_tupla_inversa(tupla):
    inversa = tuple(reversed(tupla))
    print("Tupla na ordem inversa:")
    for elemento in inversa:
        print(elemento)

# Carregar a tupla
tupla = carregar_tupla()

# Escrever a tupla na ordem inversa
escrever_tupla_inversa(tupla)
