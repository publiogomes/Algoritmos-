<<<<<<< HEAD
def soma_multiplicacao(numero):

    digitos = [int(digito) for digito in numero]

    soma = sum(digitos)

    produto = 1
    for digito in digitos:
        produto *= digito

    return soma, produto


numero = input("Digite um número positivo: ")

soma_dos_digitos, mult_dos_digitos = soma_multiplicacao(numero)

print(f"Soma dos dígitos: {soma_dos_digitos}")
=======
def soma_multiplicacao(numero):

    digitos = [int(digito) for digito in numero]

    soma = sum(digitos)

    produto = 1
    for digito in digitos:
        produto *= digito

    return soma, produto


numero = input("Digite um número positivo: ")

soma_dos_digitos, mult_dos_digitos = soma_multiplicacao(numero)

print(f"Soma dos dígitos: {soma_dos_digitos}")
>>>>>>> 3420fbf81eb404a5ed2b15adfde47adce626c897
print(f"Produto dos dígitos: {mult_dos_digitos}")