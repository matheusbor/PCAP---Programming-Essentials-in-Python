class Stack:
    def __init__(self):
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val


class CountingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__counter = 0 #precisamos inicializar ela no construtor para o objeto inicializar quando for criado

    def get_counter(self):
        return self.__counter

    def pop(self):
        self.__counter += 1 #nem precisou de for cada vez q chamar a função pop vai incrementar
        Stack.pop(self)  #só chamei a função ja implementada na superclasse
         
	

stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_counter())
