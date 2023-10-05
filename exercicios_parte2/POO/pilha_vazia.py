class QueueError(LookupError):  # Choose base class for the new exception.
    def __init__(self):
        pass
    def erro(self):
        raise LookupError


class Queue:
    def __init__(self):
        QueueError.__init__(self)
        self.fila = []
        
        
    def put(self, elem):
        self.fila.insert(0, elem)

    def get(self):
        if len(self.fila) == 0:
            raise QueueError
        x = self.fila[-1]
        del self.fila[-1]
        return x


class SuperQueue(Queue):
    def __init__(self):
        Queue.__init__(self)
        
    def isempty(self):
        
        if len(self.fila)> 0:#nao precisa do queue como herdou dele ja ta no namespace
            return False
        else:
            return True
   

que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")
