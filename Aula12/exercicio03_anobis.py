def bissexto(ano):
    if ano % 4 == 0:
        if ano % 100 != 0 or ano % 400 == 0:
            return True  # É bissexto
    return False  # Não é bissexto

#...
ano = 1805
resultado = bissexto(ano)
print(resultado)