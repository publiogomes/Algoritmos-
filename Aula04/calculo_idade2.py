from datetime import datetime
def calcular_idade(data_nascimento, data_atual):
    nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
    atual = datetime.strptime(data_atual, "%d/%m/%Y")
    diferenca = atual - nascimento

    anos = diferenca.days // 365
    meses = diferenca.days // 30
    semanas = diferenca.days // 7
    dias = diferenca.days

    return anos, meses, semanas, dias

data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")
data_atual = input("Digite a data atual (dd/mm/aaaa): ")

idade_anos, idade_meses, idade_semanas, idade_dias = calcular_idade(data_nascimento, data_atual)

print("Idade em anos:", idade_anos)
print("Idade em meses:", idade_meses)
print("Idade em semanas:", idade_semanas)
print("Idade em dias:", idade_dias)
