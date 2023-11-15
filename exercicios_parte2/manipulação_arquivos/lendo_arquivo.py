from os import strerror

objeto = open("exercicios_parte2\\manipulação_arquivos\\notas.txt","rt", encoding = "utf-8")

#print(objeto.read())

character = objeto.read(1)

contadora = 0
while character != "":
    print(character, end = "")
    character = objeto.read(1)
    contadora += 1
    if character == '5':
        character = objeto.read(1)
        print("\n ESSE:",character, "--\n")
    '''if contadora > 1000:
        break'''

objeto.close()
print("Números de caracteres: ", contadora)


