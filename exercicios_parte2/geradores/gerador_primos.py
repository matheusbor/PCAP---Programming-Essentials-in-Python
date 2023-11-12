def primos(numero):
    for i in range(numero):
        if i % 2 != 0:
            yield i


print("Cinquenta primos: ", list(primos(100)))
