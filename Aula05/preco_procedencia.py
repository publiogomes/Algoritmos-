preco_liquido = float(input("Digite o preço líquido do produto: "))
codigo_origem = int(input("Digite o código de origem do produto: "))

imposto = 0

if codigo_origem == 1:
    procedencia = "Sul"
    imposto = 0.11
elif codigo_origem == 2:
    procedencia = "Norte"
    imposto = 0.13
elif codigo_origem == 3:
    procedencia = "Nordeste"
    imposto = 0.09
elif codigo_origem == 4:
    procedencia = "Centro-Oeste"
    imposto = 0.12
elif codigo_origem == 5:
    procedencia = "Sudeste"
    imposto = 0.18
else:
    procedencia = "Origem desconhecida"

preco_final = preco_liquido + (preco_liquido * imposto)

print("Procedência:", procedencia)
print("Preço Final:", preco_final)
