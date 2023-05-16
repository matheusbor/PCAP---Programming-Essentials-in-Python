
#preenchimento e filtragem de conjuntos
conjunto = [i ** 2 for i in range(30)]
#se eu substituir a parte formadora por algum numero elevado ao índice 2 ** i, sera o conjunto das potencias desse numero

conjunto_das_potências = [3 ** i for i in range(10)]

even = [x for x in conjunto if x % 2 == 0]

odd = [ x for x in conjunto if x % 2 != 0]

print (even)
print (odd)

