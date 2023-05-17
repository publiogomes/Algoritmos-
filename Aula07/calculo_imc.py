def calcular_imc(peso, altura):
    return peso / (altura ** 2)

total_peso = 0
total_altura = 0
maior_imc = float('-inf')
menor_imc = float('inf')

for i in range(20):
    peso = float(input("Digite o peso da pessoa {}: ".format(i+1)))
    altura = float(input("Digite a altura da pessoa {}: ".format(i+1)))

    total_peso += peso
    total_altura += altura

    imc = calcular_imc(peso, altura)

    if imc > maior_imc:
        maior_imc = imc
    if imc < menor_imc:
        menor_imc = imc

media_peso = total_peso / 20
media_altura = total_altura / 20

print("Peso médio: {:.2f}".format(media_peso))
print("Altura média: {:.2f}".format(media_altura))
print("Maior IMC: {:.2f}".format(maior_imc))
print("Menor IMC: {:.2f}".format(menor_imc))
