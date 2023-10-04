
#fila2 - put insere no começo e get tira do final - dá o mesmo resultado só inverte os lados
class QueueError(LookupError):  # Choose base class for the new exception.
    def __init__(self):
        pass
    def erro(self):
        raise LookupError


class Queue:
    def __init__(self):
        self.__fila = []
        QueueError.__init__(self)

    def put(self, elem):
        self.__fila.insert(0, elem)

    def get(self):
        
        if len(self.__fila) == 0:
            return QueueError(self)
        x = self.__fila[-1]
        del self.__fila[-1]
        return x

que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")

'''#implementação de fila no sentido da vida real, entra atras sai na frente 
class QueueError(LookupError):  # Choose base class for the new exception.
    def __init__(self):
        pass
    def erro(self):
        raise LookupError


class Queue:
    def __init__(self):
        self.__fila = []
        QueueError.__init__(self)

    def put(self, elem):
        self.__fila.append(elem)

    def get(self):
        
        if len(self.__fila) == 0:
            return QueueError(self)
        x = self.__fila[0]
        del self.__fila[0]
        return x

que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")'''