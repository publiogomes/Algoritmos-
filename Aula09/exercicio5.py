import random


def simulate_dice_rolls(num_rolls):
    frequencies = [0] * 6  # Inicializa a lista de frequências com zeros para cada face do dado

    for _ in range(num_rolls):
        face = random.randint(1, 6)  # Simula o lançamento do dado
        frequencies[face - 1] += 1  # Incrementa a frequência da face sorteada

    return frequencies


num_rolls = 6000
frequencies = simulate_dice_rolls(num_rolls)

for face, frequency in enumerate(frequencies, start=1):
    print(f'Face {face}: {frequency} vezes, {frequency / num_rolls * 100:.2f}%')