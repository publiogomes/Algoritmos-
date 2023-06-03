def eh_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

numeros_primos = []
numero_atual = 101

while len(numeros_primos) < 10:
    if eh_primo(numero_atual):
        numeros_primos.append(numero_atual)
    numero_atual += 1

print(numeros_primos)

