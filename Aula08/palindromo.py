def eh_palindromo(vetor):
    reversed_vector = vetor[::-1]
    return vetor == reversed_vector

user_input = input("Digite o vetor separado por espaços: ")
vector = user_input.split()

if eh_palindromo(vector):
    print("O vetor é um palíndromo.")
else:
    print("O vetor não é um palíndromo.")
