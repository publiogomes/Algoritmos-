p1 = float(input("Digite a primeira nota: "))
p2 = float(input("Digite a segunda nota: "))
p3 = float(input("Digite a terceira nota: "))

media = float (p1+p2+p3)/3
if media >= 7:
    print(f"Sua média é {media:.1f} Aprovado")
else:
    if media >=3:
        print(f"Sua média é {media: .1f} Exame")
        nota = 12 - media
        print(f"Você precisa tirar no mínimo nota: {nota: .1f}")

    else:
        print(f"Sua média é {media: .1f} Reprovado!!")