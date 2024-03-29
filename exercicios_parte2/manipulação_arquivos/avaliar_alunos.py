class StudentsDataException(Exception):
    def __init__(self, message = "Houve um erro nos dados dos estudantes"):
        Exception.__init__(self, message)

class BadLine(StudentsDataException):
    def __init__(self, message = "A linha não está nos padrões do código"):
        StudentsDataException.__init__(self, message)

class FileEmpty(StudentsDataException):
    def __init__(self, message = "O arquivo selecionado está vazio"):
        StudentsDataException.__init__(self, message)

def verifica_existencia(name):
    existencia = False
    for i in alunos.keys():
        for key in alunos[i].keys():
            if alunos[i]['name'] == name:
                return True
    return False

def procura_aluno(name):
    for i in alunos.keys():
        for key in alunos[i].keys():
            if alunos[i]['name'] == name:
                return i
def ordem_alfabetica(dicionario):
    alfabeto = []
    for i in alunos.keys():
        for key in alunos[i].keys():
            if alunos[i]['name'] not in alfabeto:
                alfabeto.append(alunos[i]['name'])
    print("alfabeto", alfabeto)
    
    strg = "abcdefghijklmnopqrstuvxwyz"
    strg2 = strg.upper()
    posicao = []
    for i in range(len(alfabeto)):
        posicao.append([])
    print("posicao", posicao)
    i = 0
    for j in range(len(alfabeto)):#acha as posições de cada caracter em cada nome
        if i >= 3:
            i = 0
        for letter in alfabeto[j]:
            if letter in strg or letter in strg2:
                posicao[j].insert(i, strg.find(letter))
                if posicao[j][i] == -1:
                    posicao[j][i] = strg2.find(letter)
            i += 1
    print("posicao", posicao)

    lista = []

    #preciso fazer a ordem de cada item das sublistas
    lista = sorted(alfabeto)
    return lista

def print_ordenado(dicionario):
    lista = ordem_alfabetica(dicionario)
    print("lista", lista)
    j = 0
    achado = False
    while j < len(alunos.keys()):
        achado = False

        for i in alunos.keys():
            if achado:
                break
            for key in alunos[i].keys():
                if alunos[i]['name'] == lista[j]:
                    print(alunos[i]['name'], end = " ")
                    print(alunos[i]['last_name'], end = "\t\t")
                    print(alunos[i]['nota'])
                    j += 1
                    achado = True
                if achado:
                    break
name = input("Digite o nome do arquivo: ") 
try:
    lendo = open("exercicios_parte2\\manipulação_arquivos\\" + str(name), "r", encoding="utf-8")
    if len(lendo.read()) == 0:
        raise FileEmpty
    
except FileEmpty as FE:
    print("Desculpe", FE)
    exit()
except StudentsDataException as SDE:
    print("Desculpe,", SDE)
    exit()
except:
    print("Houve um erro, tente novamente")
    exit()
finally:
    lendo.close()
    

try:
        
    ler = open("exercicios_parte2\\manipulação_arquivos\\" + str(name), "r", encoding="utf-8")

    character = ler.read(1)


    alunos ={}
    i = 0
    while character != "":
        if character in "!@#$%¨&*":
            raise BadLine
        
        if i != 0:
            character = ler.read(1)

        nome = ""

        while character != " " and character != '\t':
            nome += character
            character = ler.read(1)

        if not verifica_existencia(nome):
            alunos['aluno' + str(i)] = {}
            alunos['aluno' + str(i)]['name'] = ""
            alunos['aluno' + str(i)]['last_name'] = ""
            alunos['aluno' + str(i)]['nota'] = ""
        else:
            while character == " " or character == '\t':
                character = ler.read(1)

            while character != " " and character != '\t':
                character = ler.read(1)

            while character == " " or character == '\t':
                character = ler.read(1)
        
            index_aluno = procura_aluno(nome)
            nota = float(alunos[index_aluno]['nota'])
            alunos[index_aluno]['nota'] = ""

            while character != "\n":
                alunos[index_aluno]['nota'] += character
                character = ler.read(1)

            nota += float(alunos[index_aluno]['nota'])
            alunos[index_aluno]['nota'] = str(nota)
            i += 1
            continue
        
        alunos['aluno' + str(i)]['name'] = nome
        
        while character == " " or character == '\t':
            character = ler.read(1)

        while character != " " and character != '\t':
            alunos['aluno' + str(i)]['last_name'] += character
            character = ler.read(1)

        while character == " " or character == '\t':
            character = ler.read(1)


        while character != "\n":
            alunos['aluno' + str(i)]['nota'] += character
            character = ler.read(1)
            if character == '':
                break

        i += 1
    ler.close()

    print(alunos)
    print_ordenado(alunos)
    
except BadLine as BL:
    print("Desculpe,", BL)
    exit()
except BaseException as B:
    print("Houve o erro: ", B)
    exit()