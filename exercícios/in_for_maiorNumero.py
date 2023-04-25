lista = [12, 11, 121, 212, 12]
largest = lista[0] 
#como ja atribuimos um elemento da lista a variavel n precisamos comparar ela, podemos usar um slice para pular [1:]
#mas temos que avaliar se vale a pena economizar uma comparação tendo que fazer um slice de toda lista

for i in lista:
    if i > largest: #o i irá receber os valores de cada index
        largest = i
    print(largest)
print(largest)
