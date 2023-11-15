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




name = input("Digite o nome do arquivo: ")
ler = open("exercicios_parte2\\manipulação_arquivos\\" + str(name), "r", encoding="utf-8")
alunos ={}
character = ler.read(1)

i = 0
while character != "":
    if i != 0:
        character = ler.read(1)
    print(alunos)
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
        while character == " " and character != '\t':
            character = ler.read(1)

        while character != " " and character != '\t':
            #alunos["last_name"] += character
            character = ler.read(1)

        while character == " " and character != '\t':
            character = ler.read(1)
        if len(alunos.keys()) > 1:
            index_aluno = procura_aluno(nome)#aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
            nota = float(alunos[index_aluno]['nota'])
            alunos['aluno' + str(j)]['nota'] = ""

            while character != "\n":
                alunos['aluno' + str(j)]['nota'] += character
                character = ler.read(1)

            nota += float(alunos['aluno' + str(j)]['nota'])
            alunos['aluno' + str(j)]['nota'] = str(nota)
        else:
            while character != "\n":
                alunos['aluno' + str(i)]['nota'] += character#iiiiiiiii
                character = ler.read(1)

        i += 1
        continue
    
    alunos['aluno' + str(i)]['name'] = nome
    
    while character == " " and character != '\t':
        character = ler.read(1)

    while character != " " and character != '\t':
        alunos['aluno' + str(i)]['last_name'] += character
        character = ler.read(1)

    while character == " " and character != '\t':
        character = ler.read(1)

    print(alunos)
    while character != "\n":
        alunos['aluno' + str(i)]['nota'] += character
        character = ler.read(1)

    print(i)
    i += 1
ler.close()
'''except BaseException as b:
print(b.__str__())
finlly:'''

print(alunos)

print(nome)

'''
{'aluno0': {'name': 'John', 'last_name': 'Smith', 'nota': '5'}}
{'aluno0': {'name': 'John', 'last_name': 'Smith', 'nota': '5'}, 
'aluno1': {'name': '\nAnna\tBoleyn\t4.5\nJohn\tSmith\t2\nAnna\tBoleyn', 'last_name': '11\nAndrew\tCox', 'nota': ''}}'''