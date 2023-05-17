string = input("Digite os nove caracteres numéricos: ")

# Verifica se a string tem nove caracteres
if len(string) != 9:
    print("Digite exatamente nove caracteres.")
else:
    # Separa a parte inteira da parte decimal
    parte_inteira = string[:7]
    parte_decimal = string[7:]

    # Formata a parte inteira com pontos
    parte_inteira_formatada = '.'.join(parte_inteira[i:i+3] for i in range(0, 7, 3))

    # Formata a parte decimal com vírgula
    parte_decimal_formatada = parte_decimal[:2] + ',' + parte_decimal[2:]

    # Mostra o conteúdo formatado
    print(parte_inteira_formatada + '.' + parte_decimal_formatada)
