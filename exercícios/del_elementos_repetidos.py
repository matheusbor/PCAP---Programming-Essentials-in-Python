
'''
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
x = 0
temp = []

for x in my_list:
    for i in my_list:
        if x == i:
            if x not in temp:
                temp.append(x)
            del i #isso não remove o elemento da lista
            print("Numero excluido, nova lista: ", my_list)
            
my_list = temp[:]

print("The list with unique elements only:")
print(my_list)

''' #primeiro acerto, eu estava focado na verificação para ter certeza que não atribuiria a temp números repetidos e não estava levando totalmente em conta a propriedade dos operadores in e not in de verificar se algo está ou não em um elemento, e acabei tentando fazer manualmente esta funcionalidade. podia ter dado um passo pra tras esquecer os problemas do código e analisado os elementos que o problema me deu

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
temp = []

for i in my_list: #o for ja tem uma variavel de controle embutida sendo iniciada
    if i not in temp:
        temp.append(i)
my_list = temp

print("The list with unique elements only:")
print(my_list)
#chat gpt

'''
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

i = 0
while i < len(my_list):
    if my_list[i] in my_list[:i] + my_list[i+1:]:
        del my_list[i]
    else:
        i += 1

print("The list with unique elements only:")
print(my_list)
'''#chat gpt usando índices

'''
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
temp = []

for i in my_list:
    temp.insert(0, i)
    for j in my_list:
        if temp[0] == j:
            print("Numero apagado: ", j)
            del my_list[j]
print(my_list)

print("The list with unique elements only:")
print(my_list)
'''# erro