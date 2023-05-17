idade = input("Entre com sua idade: ")

if idade.isdigit():
        idade = int(idade)
        print(idade)
else:
        print ("Você digitou uma idade inválida")
