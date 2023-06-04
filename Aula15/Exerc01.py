arquivo = open("usuarios.txt", "a", encoding="utf-8")
while True:
    nomes = input("Digite o nome e espaço utilizado: ")
    if nomes == '':
        break
    else:
        arquivo.write(nomes)
        arquivo.write("\n")

arquivo = open("usuarios.txt", encoding="utf-8")
texto = arquivo.read()
lista = texto.strip("\n")
print(lista)
arquivo.close()