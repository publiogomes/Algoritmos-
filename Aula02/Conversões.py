print ("Algoritmo de conversão de pés para polegadas, jardas e milhas")
print ("=============================================================")
pes = float(input("Digite a medida em pés: "))
polegadas = pes * 12
jardas = pes / 3
milhas = jardas / 1760
print (f"Polegadas", {polegadas})
print (f"Jardas", {jardas:.2f})
print (f"Milhas", {milhas:.2f})