
'''

drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]

hits = 0

for i in bets:
    for x in drawn:
        if i == x:
            hits += 1
            print(x)
print("Numeros iguais encontrados foram: ",hits)
'''#podemos fazer um for nested ou usar operadores membership



drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]

hits = 0

for i in bets:
    if i in drawn:
        hits += 1
print("Numeros iguais encontrados foram: ",hits)