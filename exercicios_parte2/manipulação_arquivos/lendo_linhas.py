from os import strerror

try:
    texto = open("exercicios_parte2\\manipulação_arquivos\\zen_do_python.txt", "rt", encoding="utf-8")
    contadora = 0
    linha = texto.readline()
    while linha != '':
        print(linha)
        linha = texto.readline()
        contadora += 1
    texto.close()

except IOError as erro:
    print(strerror(erro.errno))
finally:
    print("Numero de linhas: ", contadora)