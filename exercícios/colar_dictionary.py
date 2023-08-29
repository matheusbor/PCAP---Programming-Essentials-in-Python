d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}
cont = 0

for item in (d1, d2):#quando temos somente d1, o item é realmente a chave, mas quando tem os dois nessa tuple o item é o par key-value? ou o dicionario todo?

    d3.update(item)

print(d3)