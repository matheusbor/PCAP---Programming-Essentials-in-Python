from os import strerror


def ordem_frequencia(dicionario):
    alfabeto = list(dicionario.keys())
  #  print("alfabeto", alfabeto)
    frequencias = []
    for key in alfabeto:
        frequencias.append(dicionario[key])
   # print("frequencias", frequencias)

    lista = []
    maximo = 0
    while maximo > -1:
        for i in range(len(alfabeto)):
            maximo = max(frequencias)
            if frequencias[i] == maximo and alfabeto[i] not in lista:
                lista.append(alfabeto[i])
                frequencias[i] = -99
        #print("lista", lista)
       # print("frequencias", frequencias)
    
   # print("lista", lista)
    return lista


def printar_keys(lista, dicionario):
    strg = ""
    for letter in lista:
        print(letter, "->",dicionario[letter])
        strg += letter + " -> " + str(dicionario[letter]) + "\n"
    return strg
    


name = input("Digite apenas o nome do arquivo: ")

try:
    writing = open("exercicios_parte2\\manipulação_arquivos\\abc_do_python.txt", "w", encoding = "utf-8")
    writing.write("cBabAa")
    writing.close()
except IOError as e:
    print(strerror(e.errno))
    exit(e.errno)

try:
    lendo = open("exercicios_parte2\\manipulação_arquivos\\" + str(name) + ".txt", "r", encoding = "utf-8")
    
    dicionario = {}
    ler_character = lendo.read(1)
    while ler_character != "":
        if ler_character in "ABCDEFGHIJKLMNOPQRSTUVXWYZ":
            strg = ler_character.lower()
            if strg not in dicionario.keys():
                dicionario[strg] = 0
        
            dicionario[strg] += 1
            ler_character = lendo.read(1)
            continue
        if ler_character not in dicionario.keys() and ler_character not in "ABCDEFGHIJKLMNOPQRSTUVXWYZ":
            dicionario[ler_character] = 0
        
        dicionario[ler_character] += 1
        ler_character = lendo.read(1)

except IOError as e:
    print(strerror(e.errno))
    exit(e.errno)
finally:
    strg = printar_keys(ordem_frequencia(dicionario), dicionario)
try:
    writing = open("exercicios_parte2\\manipulação_arquivos\\" + str(name) + ".hist", "w", encoding = "utf-8")
    writing.write(strg)
    writing.close()
except IOError as e:
    print(strerror(e.errno))
    exit(e.errno)

