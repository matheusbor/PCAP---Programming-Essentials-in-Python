def display(digito):
    dict = { 1: "  #\n"*5,
        2:"###\n  #\n###\n#  \n###\n",
        3:"###\n  #\n###\n  #\n###\n",
        4:"# #\n# #\n###\n  #\n  #\n",
        5:"###\n#  \n###\n  #\n###\n",
        6:"###\n#  \n###\n# #\n###\n",
        7:"###\n"+"  #\n"*4,
        8:"###\n# #\n###\n# #\n###\n",
        9:"###\n# #\n###\n  #\n###\n",
        0:"###\n"+"# #\n"*3+"###\n"
    }
    return dict[digito]


numero = int(input("Digite um número"))

lista = []

while(numero > 0):
    digito = numero%10
    lista.insert(0, digito)
    print(digito)
    numero = int(numero / 10)
    
for i in range(len(lista)):
    print(display(lista[i]))

