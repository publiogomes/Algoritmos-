def primo(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

n = int(input("Digite um número inteiro: "))
resultado = primo(n)
if resultado:
    print("O número é primo (TRUE)")
else:
    print("O número não é primo (FALSE)")

