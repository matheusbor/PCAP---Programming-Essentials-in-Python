lista = [1, 2, 3, 'metade', 1., 2., 3.]
length = len(lista)

for i in range(length//2): 
    #length//2 pois eu quero um inteiro que troque apenas a metade da lista
    #precisamos desse -1 pois length não começa a contar a partir do 0 como i
    #precisamos desse -1 porque length dá o tamanho total da lista sem começar pelo 0
    lista[i], lista[length - i - 1] = lista[length -i -1], lista[i]
    print(lista)
    
    