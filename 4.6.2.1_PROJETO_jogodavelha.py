from random import randrange
board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def display_board(board = board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    # primeiro bloco
    print(('+'+'-'*7)*3+'+')
    print(('|'+" "*7)*3+'|')
    print(('|'+" "*3 + str(board[0][0]) + " "*3  + '|' ) + (" "*3 + str(board[0][1]) +" "*3  + '|') + (" "*3 + str(board[0][2]) + " "*3  + '|'))
    print(('|'+" "*7)*3+'|')
    print(('+'+'-'*7)*3+'+')

    # segundo bloco
    print(('|'+" "*7)*3+'|')
    print(('|'+" "*3 + str(board[1][0]) + " "*3  + '|' ) + (" "*3 + str(board[1][1]) +" "*3  + '|') + (" "*3 + str(board[1][2]) + " "*3  + '|'))
    print(('|'+" "*7)*3+'|')
    print(('+'+'-'*7)*3+'+')

    # terceiro bloco
    print(('|'+" "*7)*3+'|')
    print(('|'+" "*3 + str(board[2][0]) + " "*3  + '|' ) + (" "*3 + str(board[2][1]) +" "*3  + '|') + (" "*3 + str(board[2][2]) + " "*3  + '|'))
    print(('|'+" "*7)*3+'|')
    print(('+'+'-'*7)*3+'+')


def enter_move(board = board):
    # The function accepts the board current status, asks the user about their move, 
    # checks the input and updates the board according to the user's decision.

    valido = False
    while(valido == False):
        posicao = int(input("Digite o número de onde quer jogar: "))
        if posicao > 0 and posicao < 10:
            for controle1 in range(3):
                for controle2 in range(3):
                    if board[controle1][controle2] == posicao:
                        board[controle1][controle2] = "O"
                        valido = True
                        break
            if valido == False:
                print("Esta posicao ja esta preenchida tente novamente")
        else:
            print("Posicao invalida tente novamente")

    display_board()


def make_list_of_free_fields(board = board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    list_of_free_fields = []
    for controle1 in range(3):
        for controle2 in range(3):
            if board[controle1][controle2] == "X" or board[controle1][controle2] == "O":
                continue
            else:
                list_of_free_fields.append((controle1,controle2))
    return list_of_free_fields


def victory_for(board, sign):
    # The function analyzes the board status in order to check if 
    # the player using 'O's or 'X's has won the game 
    
    #verificacao do score em diagonais
    if board[0][0] == board[1][1] == board[2][2] == sign:
        print("Victory for the player using", sign)
        return
    elif board[0][2] == board[1][1] == board[2][0] == sign:
        print("Victory for the player using", sign)
        return
    #verificação do score em linhas e colunas
    for fixo in range(3):
        quantidade_linhas = 0
        quantidade_colunas = 0 #se não colocarmos ele dentro do primeiro for, o valor incrementado no segundo permanece ao longo das verificacoes de outras linhas e colunas, imprimindo várias vezes a mensagem de vitoria, continuar ...
        for variavel in range(3):
            if board[fixo][variavel] == sign: #linhas
                quantidade_linhas += 1
            if board[variavel][fixo] == sign: #colunas
                quantidade_colunas += 1
        if quantidade_linhas == 3 or quantidade_colunas == 3:
            print("Victory for the player using", sign)
            return 
    # verificacao de empate
    if len(make_list_of_free_fields(board)) == 0:
        return 1
    else: 
        return 2
    

def draw_move(board = board):
    # The function draws the computer's move and updates the board.

    vazios = make_list_of_free_fields(board)
    if (1,1) not in vazios: #sera que economiza processamento deixando o else como a primeira jogada? já que so vai uma vez
        aleatorio = randrange(len(vazios))
        (row, column) = vazios[aleatorio - 1] #por causa do len
        board[row][column] = "X"
    else:
        board[1][1] = "X"

    display_board()


def status():
    resultado1 = victory_for(board, "X")
    resultado2 = victory_for(board, "O")

    if resultado1 == resultado2 == 1:
        print("The game ended as a tie")
        return True
    elif resultado1 == resultado2 == 2:
        print("No one won, this game must continue")
        return False
    else:
        return True #porque alguem ganhou, seria o return 3


ended = False

while(ended == False):
    draw_move()
    ended = status()
    if ended:
        continue

    enter_move()
    ended = status()
    if ended:
        continue


''' 
#testagem
display_board(board)
#make_list_of_free_fields(board)
#enter_move(board)
#display_board(board)
#draw_move(board)
#display_board(board)
victory_for(board, "X")
'''
