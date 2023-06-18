x = int(input("digite"))
y = int(input("digitee"))

x = x / y
y = y / x

print(y)


potencia_10 = [10 ** i for i in range(10)]

menores_que_10000 = [x for x in potencia_10 if x < 10000]


menores_que_10000 = []
for x in potencia_10:
    if x < 10000:
       menores_que_10000.append(x)

print(menores_que_10000)