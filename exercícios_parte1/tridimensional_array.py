rooms = [[[False for room in range(20)] for floors in range(15)] for buildings in range(3)]

rooms[1][9][13] = True #ocupa o quarto  

rooms[0][4][1] = False #libera o quarto

vacancy = 0

for unoccupied_room in rooms[2][14]:
    if rooms[2][14][unoccupied_room] == False:
        vacancy += 1
print("The number of unoccupied rooms in the third building at the fifteenth floor is: ", vacancy)