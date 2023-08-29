EMPTY = "     "
ROOK = "ROOK "
cavalo = "HORSE"
bispo = "BISPO"
king = "KING "
queen = "QUEEN"
board = []

board = [[EMPTY for elemento in range(8)] for linha in range(8)]

board[0][0] = ROOK
board[0][7] = ROOK
board[7][0] = ROOK
board[7][7] = ROOK

board [0][1] = cavalo
board [0][6] = cavalo
board [7][1] = cavalo
board [7][6]= cavalo

board [0][2] = bispo
board [0][5] = bispo
board [7][2] = bispo
board [7][5] = bispo

board [0][3] = queen
board [0][4] = king
board [7][3] = queen
board [7][4] = king

board[1] = ["PAWN " for elemento in range(8)] #preenchi cada elemento da lista com a string, se tivesse usado slicing teria dado uma letra para cada posição
board[6] = ["PAWN " for elemento in range(8)]

'''for linha in board:
    print(linha) #a variavel de controle não toma 0,1,2 como seus valores; ela toma OS ELEMENTOS nessas posições como seus valores
'''
for linha in board:
    print("|".join(linha))
    print("-" * 46)