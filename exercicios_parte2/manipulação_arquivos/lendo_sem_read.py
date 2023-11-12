from os import strerror

contadora_linha = 0
contadora_character = 0

try:
    for linha in open("exercicios_parte2\\manipulação_arquivos\\zen_do_python.txt", "r", encoding= "utf-8"):
        contadora_linha += 1
        for character in linha:
            contadora_character += 1
            print(character, end="")

except IOError as erro:
    print(strerror(erro.errno))
finally:
    print()
    print("Numero de linhas: ", contadora_linha)
    print("Numero de caracteres: ", contadora_character)