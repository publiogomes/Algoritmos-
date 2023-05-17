nome = input("Digite seu 1º nome: ")
nome_meio = input("Digite seu nome do meio: ")
sobrenome = input("Digite seu sobrenome: ")

nome_completo = nome+ ' ' +nome_meio+ ' ' +sobrenome
print(f"Nome completo: {nome_completo}")

#criptografia
nome_cripto = '' #vazio
for indice in range(0, len(nome_completo)):
    nome_cripto += chr(ord(nome_completo[indice])+1)
    print(f"Nome Cripto: {nome_cripto}")


