arquivo = open("usuarios.txt", encoding="utf-8")
texto = arquivo.read()
lista = texto.strip("\n")
print(lista)
arquivo.close()

