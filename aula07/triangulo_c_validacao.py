base = float(input("Entre com a base do triângulo: "))
while base <=0:
    base = float(input("Digite a base do triângulo menor ou maior do que 0: ")) #aqui é para validar se o usuário entrou com dados corretos

#pode fazer nessa lógica acima ou usando o método abaixo

while True:
    altura = float(input("Digite a altura do triângulo: "))
    if altura > 0:
        break

area = (base * altura) / 2
print((f"A área do triângulo = {area:.2f}"))



