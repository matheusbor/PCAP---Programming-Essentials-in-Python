board = []
EMPTY = ' '
linha = ' '
for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)
    

print (board)

board = [[EMPTY for i in range(8)] for x in range(8)] #qual a diferença de usar parenteses para colchetes aqui - [] é lista e () é tupla
   #         item a ser repetido + repetição - tamanho - condição (opcional)

print (board)

lista_bidimensional = [[linha for i in range(8)] for i in range(8)]
print(lista_bidimensional)