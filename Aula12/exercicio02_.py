def primo(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

print("Os 50 primeiros números primos são: ")
i, n = 2, 0
coluna = 1
while n <= 50:
    if primo(i):
        print(i, end=" - ")
        n += 1
    i += 1
    if coluna > 15:
        print()
        coluna = 1
