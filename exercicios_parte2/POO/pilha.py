class stack:
	def __init__(self):# função construtora
		self.__stack_lista = []

	def push(self, val):#função de atividade / método
		self.__stack_lista.append(val)

	def pop(self):
		x = self.__stack_lista[-1]
		del self.__stack_lista[-1]
		return x
	
objeto = stack()
objeto2 = stack()

class soma_pilha(stack):
	def __init__(self):
		stack.__init__(self)
		self.__sum = 0
	
	def push(self, val):
		self.__sum += val
		stack.push(self, val) #to chamando o método da superclasse e deixa a implementação dela resolver
	
	def pop(self):
		val = stack.pop(self) #não preciso chamar a função duas vezes porque excluiria duas vezes
		self.__sum -= val
		return val
	def get_soma(self):
		return self.__sum


objeto3 = soma_pilha()

for i in range(10):
	objeto3.push(i)
print("A soma é: ",objeto3.get_soma()) 

for i in range(10):
	objeto3.pop()
print("Com a exclusão a soma é: ",objeto3.get_soma())


''' objeto.push(5) # nossa função se torna um método, lembrar de chamar como método
objeto2.push(objeto.pop())

print(objeto2.pop())
#print(len(objeto.stack_lista)) não é mais possível por ser privada'''
