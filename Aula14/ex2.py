<<<<<<< HEAD
def primo(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                return False
        return True

def cont_primo(n):
    cont = 0
    for num in range(2, n + 1):
        if primo(num):
            cont += 1
    return cont

num = int(input("Digite um número inteiro e positivo: "))

prime_list = [i for i in range(2, num + 1) if primo(i)]
prime_sum = sum(prime_list)

print("Lista de números primos:", prime_list)
print("Quantidade de números primos:", cont_primo(num))
=======
def primo(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                return False
        return True

def cont_primo(n):
    cont = 0
    for num in range(2, n + 1):
        if primo(num):
            cont += 1
    return cont

num = int(input("Digite um número inteiro e positivo: "))

prime_list = [i for i in range(2, num + 1) if primo(i)]
prime_sum = sum(prime_list)

print("Lista de números primos:", prime_list)
print("Quantidade de números primos:", cont_primo(num))
>>>>>>> 3420fbf81eb404a5ed2b15adfde47adce626c897
print("Soma dos números primos:", prime_sum)