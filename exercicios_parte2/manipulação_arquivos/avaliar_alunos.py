class StudentsDataException(Exception):
    pass


class BadLine(StudentsDataException):
    # Write your code here.
    pass


class FileEmpty(StudentsDataException):
    pass

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
    i = 0
    for j in 
    for letter in alfabeto[i]:#vai ordenar apenas pela primeira letra
        if letter in strg or letter in strg2:
            posicao.insert(i, strg.find(letter))
            if posicao[i] == -1:
                posicao[i] = strg2.find(letter)
        i += 1
    print("posicao", posicao)
    lista = []
    for i in range(len(alfabeto)):
        minimo = min(posicao)
        if posicao[i] == minimo:
            lista.append(alfabeto[i])
            posicao[i] = 99
    return lista

def print_ordenado(dicionario):
    lista = ordem_alfabetica(dicionario)
    print("lista", lista)
    j = 0
    while j < len(alunos.keys()):
        for i in alunos.keys():
            for key in alunos[i].keys():
                if alunos[i]['name'] == lista[j]:
                    print(alunos[i]['name'], end = " ")
                    print(alunos[i]['last_name'], end = "\t\t")
                    print(alunos[i]['nota'])
                    j += 1



name = input("Digite o nome do arquivo: ")
ler = open("exercicios_parte2\\manipulação_arquivos\\" + str(name), "r", encoding="utf-8")
alunos ={}
character = ler.read(1)

i = 0
while character != "":
    if i != 0:
        character = ler.read(1)
    #print(alunos)
    nome = ""

    while character != " " and character != '\t':
        nome += character
        character = ler.read(1)
        #i+= 1
    if not verifica_existencia(nome):
        alunos['aluno' + str(i)] = {}
        alunos['aluno' + str(i)]['name'] = ""
        alunos['aluno' + str(i)]['last_name'] = ""
        alunos['aluno' + str(i)]['nota'] = ""
    else:
        while character == " " or character == '\t':
            character = ler.read(1)

        while character != " " and character != '\t':
            #alunos['aluno' + str(i)]['last_name'] += character pois ele já existe
            character = ler.read(1)

        while character == " " or character == '\t':
            character = ler.read(1)
    
        index_aluno = procura_aluno(nome)#aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
        nota = float(alunos[index_aluno]['nota'])
        alunos[index_aluno]['nota'] = ""

        while character != "\n":
            alunos[index_aluno]['nota'] += character
            character = ler.read(1)

        nota += float(alunos[index_aluno]['nota'])
        alunos[index_aluno]['nota'] = str(nota)

        '''while character != "\n":
            alunos[index_aluno]['nota'] += character#iiiiiiiii
            character = ler.read(1)'''

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

    #print(alunos)
    #print("caracter",character)
    while character != "\n":
        alunos['aluno' + str(i)]['nota'] += character
        character = ler.read(1)
        if character == '':
            break

    #print(i)
    i += 1
ler.close()
'''except BaseException as b:
print(b.__str__())
finlly:'''

print(alunos)
print_ordenado(alunos)

#print(nome)

'''
{'aluno0': {'name': 'John', 'last_name': 'Smith', 'nota': '5'}}
{'aluno0': {'name': 'John', 'last_name': 'Smith', 'nota': '5'}, 
'aluno1': {'name': '\nAnna\tBoleyn\t4.5\nJohn\tSmith\t2\nAnna\tBoleyn', 'last_name': '11\nAndrew\tCox', 'nota': ''}}'''