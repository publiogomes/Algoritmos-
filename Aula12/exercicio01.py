def verificar_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

numero = int(input("Digite um número inteiro: "))
resultado = verificar_par(numero)

if resultado:
    print("O número é par (TRUE)")
else:
    print("O número é ímpar (FALSE)")
