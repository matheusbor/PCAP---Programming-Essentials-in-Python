from os import strerror


try:
    fonte = open("exercicios_parte2\manipulação_arquivos\zen_do_python.txt", "r", encoding="utf-8")

except IOError as e:
    print(strerror(e.errno))
    exit(e.errno)


try:
    destino = open("exercicios_parte2\manipulação_arquivos\destino.txt", "w", encoding = "utf-8")

except IOError as e:
    print(strerror(e.errno))
    exit(e.errno)


total = 0
try:
    lidos = fonte.read(100)

    while lidos != "":
        escritos = destino.write(lidos)
        total += escritos#total guarda a quantidade de caracteres que foi lida
        lidos = fonte.read(100)
except IOError as e:
    print(strerror(e.errno))
    exit(e.errno)
finally:
    print("Numero escritos: ", total)