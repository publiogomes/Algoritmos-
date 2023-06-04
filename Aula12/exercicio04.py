def calcular_mdc(a, b):
    # Verificar se algum dos números é zero
    if a == 0 or b == 0:
        return max(abs(a), abs(b))

    # Aplicar o algoritmo de Euclides
    while b != 0:
        a, b = b, a % b

    # O valor absoluto de 'a' será o MDC
    return abs(a)

print(calcular_mdc(12, 18))