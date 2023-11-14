from os import strerror


def ordem_alfabetica(dicionario):
    alfabeto = list(dicionario.keys())
    
    strg = "abcdefghijklmnopqrstuvxwyz"
    strg2 = strg.upper()
    posicao = []
    i = 0
    for letter in alfabeto:
        if letter in strg or letter in strg2:
            posicao.insert(i, strg.find(letter))
            if posicao[i] == -1:
                posicao[i] = strg2.find(letter)
        i += 1
    
    lista = []
    for i in range(len(alfabeto)):
        minimo = min(posicao)
        if posicao[i] == minimo:
            lista.append(alfabeto[i])
            posicao[i] = 99
    return lista



def printar_keys(lista, dicionario):
    for letter in lista:
        print(letter, "->",dicionario[letter])


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
    while ler_character != "":
        if ler_character not in dicionario.keys():
            dicionario[ler_character] = 0
        
        dicionario[ler_character] += 1
        ler_character = lendo.read(1)

except IOError as e:
    print(strerror(e.errno))
    exit(e.errno)
except BaseException as b:
    print(strerror(b.errno))
    exit(b.errno)
finally:
    printar_keys(ordem_alfabetica(dicionario), dicionario)