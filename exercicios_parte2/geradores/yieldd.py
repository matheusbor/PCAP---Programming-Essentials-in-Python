def gerador(numero):
    for i in range(numero):
        yield i

print(gerador(10))

for valor in gerador(3):
    print(valor)

print(list(gerador(20)))

for i in range(30):
    if i in gerador(10):
        print(i)