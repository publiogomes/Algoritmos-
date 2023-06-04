#exercicio do while
import math
e = 0
n = int(input("Digite um número inteiro positivo: "))
b = int(input("digite o valor da base: "))
i = 1
while i <=n:
    e = e + math.pow(b, i)
    i = i + 1

print((f"O valor de E = {e:.2f}"))

#esse é a mesma lógica do exercicio2