lista1 = []
lista2 = []

# Carregando a primeira lista
print("Digite os elementos da primeira lista:")
for i in range(10):
    elemento = int(input("Elemento {}: ".format(i+1)))
    lista1.append(elemento)

# Carregando a segunda lista
print("\nDigite os elementos da segunda lista:")
for i in range(10):
    elemento = int(input("Elemento {}: ".format(i+1)))
    lista2.append(elemento)

# Criando o conjunto da união das duas listas
conjunto_uniao = set(lista1 + lista2)

# Imprimindo o conjunto da união
print("\nConjunto da união das duas listas:")
print(conjunto_uniao)