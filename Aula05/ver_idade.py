ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = 2023
idade = ano_atual - ano_nascimento

print("Idade:", idade)

if idade >= 16:
    print("Você já tem idade para votar.")
else:
    print("Você ainda não tem idade para votar.")

if idade >= 18:
    print("Você já pode obter a Carteira de Habilitação.")
else:
    print("Você ainda não tem idade para obter a Carteira de Habilitação.")

