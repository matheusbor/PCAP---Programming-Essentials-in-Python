from os import strerror

name = input("Digite o nome do arquivo: ")

try:
    writing = open("exercicios_parte2\\manipulação_arquivos\\abc_do_python.txt", "w", encoding = "utf-8")
    writing.write("aBc")
    writing.close()
except IOError as e:
    print(strerror(e.errno))
    exit(e.errno)

try:
    lendo = open("exercicios_parte2\\manipulação_arquivos\\" + str(name), "r", encoding = "utf-8")
    
    dicionario = {}
    ler_character = lendo.read(1)
    contadora = 0
    while ler_character != "":
        if ler_character not in dicionario.keys():
            dicionario[ler_character] = 0
        contadora += 1
        dicionario[ler_character] += 1
        ler_character = lendo.read(1)

except IOError as e:
    print(strerror(e.errno))
    exit(e.errno)
finally:
    print(dicionario)