numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

opcao = int(input("Escolha uma operação (1-Média, 2-Diferença, 3-Produto, 4-Divisão): "))

if opcao == 1:
    media = (numero1 + numero2) / 2
    print("A média é:", media)
elif opcao == 2:
    diferenca = abs(numero1 - numero2)
    print("A diferença é:", diferenca)
elif opcao == 3:
    produto = numero1 * numero2
    print("O produto é:", produto)
elif opcao == 4:
    if numero2 != 0:
        divisao = numero1 / numero2
        print("A divisão é:", divisao)
    else:
        print("Não é possível dividir por zero.")
else:
    print("Opção inválida.")
