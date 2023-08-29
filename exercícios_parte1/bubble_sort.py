'''lista = [5, 3, 66,47,4]

for i in range(len(lista) - 1):
    if lista [i]<lista[i + 1]:
        print("OK")
    else:
        lista[i], lista[i + 1] = lista[i + 1], lista[i]

print(lista) 
'''
#ele passa da esquerda pra direita não conseguindo fazer numeros com index distantes interagir

lista = [5, 3, 66,47,4]
swapped = True

while swapped:
    swapped = False #because this goes atributte as false every loop and if have a swap to do, swapped receive true and continue
    for i in range(len(lista) - 1):
        if lista [i]>lista[i + 1]:
            swapped = True 
            '''isso não vai fazer que numeros trocados la pro meio da lista não sejam ordenados? pois vai começar a verificar a partir do 0 e se eles nao tiverem não vai ordenar o resto /// não porque temos um loop nested, a cada passada do for ele vai repetir 4 vezes varrendo toda lista e se ao menos 1 precisar de troca ele vai trocar e atribuir True, o swapped não precisa ser true para toda repetição do if visto que essa condição não tem nada haver com o for, e atribuindo dentro do if quando houver a ultima troca - como o sistema n sabe que foi a ultima troca - ele ainda roda de novo mais uma passagem for e verifica, e o for por sua vez não precisando de nenhuma troca não atribui True fazendo o loop while acabar'''
            lista[i], lista[i + 1] = lista[i + 1], lista[i]
print(lista)

list = [ 523,56346,346,457,]
list.sort() #native method for sort
print(list)
