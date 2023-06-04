def verificar_par(x):
    return (x%2 ==0)

numero = int(input("Digite um número inteiro: "))
resultado = verificar_par(numero)

if resultado:
    print("O número é par (TRUE)")
else:
    print("O número é ímpar (FALSE)")