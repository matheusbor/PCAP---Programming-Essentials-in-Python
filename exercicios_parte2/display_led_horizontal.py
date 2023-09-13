

def print_number(num):
    for i in range(len(num)):
        digito = int(num[i])
       #primeira linha
        if digito != 1 and digito != 4:
            print("###", end=" ")
        elif digito == 1:
            print("  #", end = " ")
        elif digito == 4:
            print("# #", end = " ")
 

print_number(input("Enter the number you wish to display: "))
