
  # ### ### # # ### ### ### ### ### ### 
  #   #   # # # #   #     # # # # # # # 
  # ### ### ### ### ###   # ### ### # # 
  # #     #   #   # # #   # # #   # # # 
  # ### ###   # ### ###   # ### ### ###

def print_number(num):
    
    for linha in range(5):
        for i in range(len(num)):
            digito = int(num[i])
            
            if linha == 0:
                if digito != 1 and digito != 4:
                    print("###", end="  ")
                elif digito == 1:
                    print("  #", end = "  ")
                elif digito == 4:
                    print("# #", end = "  ")
                 
            elif linha == 1:
                if digito == 1 or digito == 2 or digito == 3 or digito == 7:
                    print("  #", end = "  ")
                elif digito == 5 or digito == 6:
                    print("#  ", end = "  ")
                else:
                    print("# #", end = "  ")

            elif linha == 2:
                if digito == 1 or digito == 7:
                    print("  #", end = "  ")
                elif digito == 0:
                    print("# #", end= "  ")
                else:
                    print("###", end = "  ")

            elif linha == 3:
                if digito == 0 or digito == 6 or digito == 8:
                    print("# #", end = "  ")
                elif digito == 2:
                    print("#  ", end = "  ")
                else:
                    print("  #", end = "  ")
            
            elif linha == 4:
                if digito == 1 or digito == 7 or digito == 4:
                    print("  #", end = "  ")
                else:
                    print("###", end = "  ")
        print()


print_number(input("Enter the number you wish to display: "))
