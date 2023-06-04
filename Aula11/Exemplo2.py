idades = {
    'ana': 34,
    'pedro': 31,
    'jose': 45,
    'joao': 18,
  }

maior = 0
nome_maior = ''
for nome in idades.keys():
    if len(nome) > maior:
        maior = len(nome)
        nome_maior = nome

    print(f" O maior nome é: {nome_maior} e a sua idade é: {idades.get(nome_maior)}")