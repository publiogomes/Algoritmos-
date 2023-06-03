import random

# Dicionário para armazenar a contagem de cada soma
frequencia = {i: 0 for i in range(2, 13)}

# Simulação de 30.000 jogadas
num_jogadas = 30000

for _ in range(num_jogadas):
    # Rolar os dados
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)

    # Calcular a soma
    soma = dado1 + dado2

    # Atualizar a contagem da soma
    frequencia[soma] += 1

# Calcular a frequência relativa de cada soma
frequencia_relativa = {soma: contagem / num_jogadas for soma, contagem in frequencia.items()}

# Imprimir a frequência relativa de cada soma
for soma, freq_rel in frequencia_relativa.items():
    print(f'Soma {soma}: {freq_rel:.4f}')

# Verificar se o valor 7 corresponde a 1/6 das jogadas
frequencia_7 = frequencia[7]
freq_rel_7 = frequencia_relativa[7]
esperado_7 = num_jogadas / 6

print(f'\nFrequência de 7: {frequencia_7} ({freq_rel_7:.4f})')
print(f'Esperado para 7: {esperado_7}')

