soma = 0
n = 0
for x in range(1,11):
    idade = int(input(f"Digite a {x}a. idade: "))
    soma = soma + idade
    n = n + 1
    if x == 3:
        break # aqui ele sai da estrutura e finaliza.
    print(x)
    print(n)
    media = soma/x
    print(f"A média das idades é igual a {media:.2f}")
