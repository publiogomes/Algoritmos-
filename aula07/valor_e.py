import math
e = 0
n = int(input("Digite um número inteiro positivo: "))
for i in range(1, n+1):
    e = e + math.pow(2, i) # você pode colocar tbm e = e + 2**1, e não importaria math
    print((f"O valor de E = {e:.2f}"))
