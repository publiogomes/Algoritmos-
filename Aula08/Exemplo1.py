nome = input("Digite seu nome: ")
data = input ("Digite a data (dd/mm/aaaa): ")
print (f"Ola {nome}, tenha uma excelente noite!")
print (type(nome))
print (len(nome))

for i in range(len(nome)-1, -1, -1):
    print(nome[i], end="\n")

    print (nome[::-1])

a=5.0
novo_nome = nome.replace('a', '@')
print(novo_nome.split())
print(data.split("/"))
print(novo_nome.lower().title())