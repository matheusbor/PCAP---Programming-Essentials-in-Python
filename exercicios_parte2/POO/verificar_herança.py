class Escola:
    def __init__(self, turma, matéria):
        self.turma = turma
        self.materia = matéria
    def __hello(self):
        return "hello"
aluno = Escola(1001, "matematica")

print(aluno)

class Universidade(Escola):
    def __init__(self, turma, materia, curso):   
        Escola.__init__(self, turma, materia)
        self.curso = curso
        
formando = Universidade(1001, "cálculo","engenharia")

print(isinstance(formando, Universidade))
print(issubclass(Universidade, Escola))
