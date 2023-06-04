from funcoes import jogar_dado
import time # para criar um delay entre as jogadas

print("Vamos jogar dados!\n")

pontos_jogador = 0
pontos_computador = 0
rodada = 1

while True:
    input("Pressione enter para jogar o dado...")
    jogada_jogador = jogar_dado()
    jogada_computador = jogar_dado()

    print("\nJogada da rodada", rodada)
    print("Jogador:", jogada_jogador)
    print("Computador:", jogada_computador)

    if jogada_jogador > jogada_computador:
        pontos_jogador += 1
        print("Jogador venceu a rodada!\n")
    elif jogada_computador > jogada_jogador:
        pontos_computador += 1
        print("Computador venceu a rodada!\n")
    else:
        print("Empate!\n")

    rodada += 1
    time.sleep(3)

    if rodada > 5:  # definimos 5 rodadas para o jogo
        break

print("Fim do jogo!")
print("Placar final:")
print("Jogador:", pontos_jogador)
print("Computador:", pontos_computador)
if pontos_jogador > pontos_computador:
    print("Você ganhou!")
elif pontos_computador > pontos_jogador:
    print("Computador ganhou!")
else:
    print("Empatou!")
