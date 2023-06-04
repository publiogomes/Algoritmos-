def calcular_volume_esfera(raio):
    volume = (4/3) * 3.14159 * (raio ** 3)
    return volume

'''Nessa função, raio é o parâmetro que representa o raio da esfera. O volume é calculado usando a fórmula v = (4/3) * pi * (raio ** 3), onde pi é uma aproximação do valor de π (3.14159).

Você pode chamar a função da seguinte forma para calcular o volume de uma esfera com raio 5, por exemplo: '''

raio = 5
volume_esfera = calcular_volume_esfera(raio)
print(volume_esfera)

