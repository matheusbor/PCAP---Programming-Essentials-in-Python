class Pessoa:
    população = 0
    __saude = True
    def __init__(self, nome):
        Pessoa.população += 1
        self.name = nome
        self.__age = 20
        self.__stk = []
    def __teste(self):
        Pessoa.olhos = 'green'
    def teste3(self):
        return "teste"
    def teste4(self):
        self.__stk.append(1)
        return self.__stk

class Individuo(Pessoa):
    '''
    def __init__(self, nome):
        Pessoa.__init__(self, nome)'''
    

    def teste2(self):
        self._Pessoa__teste() 
        print(self.olhos)
        pass

trabalhador = Individuo("marcos")

print(Pessoa.população, Pessoa._Pessoa__saude, trabalhador.população, sep = "\t")#variaveis de classe
print( trabalhador.teste3(), trabalhador.teste4(), sep = "\t")#metodos
print(trabalhador.name, trabalhador._Pessoa__age, sep = "\t")#variaveis de instancia
trabalhador.teste2()