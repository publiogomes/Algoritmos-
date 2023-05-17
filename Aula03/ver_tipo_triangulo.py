a = float(input("valor lado a: "))
b = float(input("valor lado b: "))
c = float(input("valor lado c: "))

if a + b > c and a + c > b and b + c > a:
    print("Os lados formam um Triângulo")

if a == b and b == c:
    print("Triângulo equilátero")

if b + c > a:
    print("Triângulo isósceles")

else:
    print("Não é um triângulo")
