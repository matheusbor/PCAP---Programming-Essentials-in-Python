
lista = [10 if x >= 10 else 0 for x in range(20)]
print(lista)

for i in (10 if x >= 10 else 0 for x in range(20)):
    print(i, end = "\t")