class Pessoa:
    população = 0
    __saude = True
    def __init__(self, nome):
        Pessoa.população += 1
        self.name = nome
        self.__age = 20
    def __teste(self):
        Pessoa.olhos = 'green'

class Individuo(Pessoa):
    '''
    def __init__(self, nome):
        Pessoa.__init__(self, nome)'''
    

    def teste2(self):
        self._Pessoa__teste() 
        print(self.olhos)
        pass

trabalhador = Individuo("marcos")

print(Pessoa.população, Pessoa._Pessoa__saude, trabalhador.name, trabalhador._Pessoa__age, sep = "\t")
trabalhador.teste2()