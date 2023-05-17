sal_min = float(input("Digite o valor do salário mínimo: "))
quilowatts_consumidos = float(input("Digite a quantidade de quilowatts consumida pela residência: "))

valor_quilowatt = sal_min / 8
valor_total = valor_quilowatt * quilowatts_consumidos
valor_desconto = valor_total * 0.85

print("a) O valor de cada quilowatt em reais é: R$", valor_quilowatt)
print("b) O valor a ser pago pela residência em reais é: R$", valor_total)
print("c) O valor a ser pago com desconto de 15% em reais é: R$", valor_desconto)
