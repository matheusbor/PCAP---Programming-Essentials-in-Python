
'''list = [1212 , 1212 , 1234 ,1241]
to_find = 1212

found = False


for i in list:
    found = i == to_find
    if found:
        break

if found:
    print("Element found: ", i)
else:
    print("element absent") ''' #não usamos pois não podemos determinar o index do valor encontrado

list = [1, 42354,35635,457667,4]
to_find = 35635 #variável valor alvo para achar na lista

found = False #variável do estado da pesquisa

for i in range (len(list)):
    found = list[i] == to_find
    if found:
        break
if found:
    print("elemente found at index: ", i)
else:   
    print("elemente not found, absent")


