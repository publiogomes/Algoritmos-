def animais(cabeca, pes):
    coelho = (pes - (2*cabeca))/2
    pato = cabeca - coelho
    return coelho,pato

cabeca=int(input("Digite a quantidade de cabeças: "))
pes=int(input("Digite a quantidade de pes: "))
resultado = animais (cabeca,pes)
print("A soma de coelhos e patos, respectivamente é: ", resultado)