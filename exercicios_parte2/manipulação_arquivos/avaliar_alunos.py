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
    '''for i in range(len(alfabeto)):
        minimo = min(posicao)
        if posicao[i] == minimo:
            lista.append(alfabeto[i])
            posicao[i] = 99'''
    ordem = [0,0,0]
    #preciso fazer a ordem de cada item das sublistas
    for i in range(len(alfabeto) - 1):
        ordem[i] = 0
        ordem[i + 1] = 0
        for j in range(len(alfabeto)):
            if posicao[i][j] in posicao and posicao [i+1][j] in posicao:

                if posicao[i][j] == posicao[i + 1][j]:
                    continue
                if posicao[i][j] < posicao[i + 1][j]:
                    ordem[i] += 1
                elif posicao[i + 1][j] < posicao[i][j]:
                    ordem[i + 1] += 1

        if ordem[i] > ordem[i + 1]:
            maior = i
            ordem[i + 2] = 0
            for j in range(len(alfabeto)):
                if posicao[i][j] in posicao and posicao [i+2][j] in posicao:

                    if posicao[i][j] == posicao[i + 2][j]:
                        continue
                    if posicao[i][j] < posicao[i + 2][j]:
                        ordem[i] += 1
                    elif posicao[i + 2][j] < posicao[i][j]:
                        ordem[i + 2] += 1

        elif ordem[i+ 1] > ordem[i]:
            maior = i + 1
            ordem[i + 2] = 0
            for j in range(len(alfabeto)):
                if posicao[maior][j] in posicao and posicao [i+2][j] in posicao:

                    if posicao[maior][j] == posicao[i + 2][j]:
                        continue
                    if posicao[maior][j] < posicao[i + 2][j]:
                        ordem[maior] += 1
                    elif posicao[i + 2][j] < posicao[maior][j]:
                        ordem[maior + 2] += 1
        print(ordem)
    return lista

def print_ordenado(dicionario):
    lista = ordem_alfabetica(dicionario)
    print("lista", lista)
    j = 0
    achado = False
    while j < len(alunos.keys()):
        achado = False
        print("j", j)
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