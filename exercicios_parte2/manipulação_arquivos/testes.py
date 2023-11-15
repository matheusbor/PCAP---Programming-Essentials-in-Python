alunos = {}

alunos['alunos'] = {}
alunos['alunos2'] = {}
alunos['alunos2']['name'] = ""

alunos['alunos']['name'] = "matheus"
alunos['alunos']['idade'] = "20"



def verifica_existencia(name):
    existencia = False
    for key in alunos['alunos'].keys():
        for i in alunos.keys():
            if alunos[i]['name'] == name:
                return True
    return False


name = 'a'
print(name)
name += name
print(name)
print(alunos.keys())
print(alunos['alunos'].keys())
print(alunos['alunos2'].keys())
print(verifica_existencia('caio'))
