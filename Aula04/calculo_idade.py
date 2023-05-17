from datetime import date
def calcular_idade(ano_nascimento, ano_atual):
    data_nascimento = date(ano_nascimento, 1, 1)
    data_atual = date(ano_atual, 1, 1)
    idade = data_atual.year - data_nascimento.year

    meses = idade * 12
    dias = idade * 365
    semanas = dias // 7

    return idade, meses, dias, semanas

ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))

idade, meses, dias, semanas = calcular_idade(ano_nascimento, ano_atual)

print("Idade em anos:", idade)
print("Idade em meses:", meses)
print("Idade em dias:", dias)
print("Idade em semanas:", semanas)
