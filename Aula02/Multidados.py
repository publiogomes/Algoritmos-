nascimento = int(input("Digite o ano do seu nascimento: "))
anoatual = int(input("Digite em qual ano estamos: "))
idade = anoatual-nascimento
meses = idade * 12
semanas = idade * 53
dias = idade * 365
print(f"idade: {idade} anos, {meses} meses")
print(f"{semanas} semanas e {dias} dias")