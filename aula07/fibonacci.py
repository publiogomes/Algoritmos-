def fibonacci(n):
    sequence = [0, 1]  # Inicializa a sequência com os dois primeiros números: 0 e 1

    for i in range(2, n):
        next_number = sequence[i - 1] + sequence[i - 2]  # Calcula o próximo número da sequência
        sequence.append(next_number)  # Adiciona o próximo número à sequência

    return sequence[:n]  # Retorna os n primeiros números da sequência


# Calcula e exibe os 10 primeiros números da sequência de Fibonacci
fib_numbers = fibonacci(10)
for number in fib_numbers:
    print(number)
