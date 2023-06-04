<<<<<<< HEAD
def animais(cabeca, pes):
    coelho = (pes - (2*cabeca))/2
    pato = cabeca - coelho
    return coelho,pato

cabeca=int(input("Digite a quantidade de cabeças: "))
pes=int(input("Digite a quantidade de pes: "))
resultado = animais (cabeca,pes)
=======
def animais(cabeca, pes):
    coelho = (pes - (2*cabeca))/2
    pato = cabeca - coelho
    return coelho,pato

cabeca=int(input("Digite a quantidade de cabeças: "))
pes=int(input("Digite a quantidade de pes: "))
resultado = animais (cabeca,pes)
>>>>>>> 3420fbf81eb404a5ed2b15adfde47adce626c897
print("A soma de coelhos e patos, respectivamente é: ", resultado)