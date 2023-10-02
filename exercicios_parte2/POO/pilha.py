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

objeto.push(5) # nossa função se torna um método, lembrar de chamar como método
objeto2.push(objeto.pop())

print(objeto2.pop())
#print(len(objeto.stack_lista)) não é mais possível por ser privada