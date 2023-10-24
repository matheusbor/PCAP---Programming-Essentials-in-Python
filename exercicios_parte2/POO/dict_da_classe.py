

class Classy:
    varia = 1
    def __init__(self):
        self.var = 2

    def method(self):
        pass

    def __hidden(self):
        pass


for key in Classy.__dict__.keys():
    print(key, Classy.__dict__[key])


'''__module__ __main__
varia 1
__init__ <function Classy.__init__ at 0x7ff9ffcc8320>
method <function Classy.method at 0x7ff9ffcc83b0>
_Classy__hidden <function Classy.__hidden at 0x7ff9ffcc8440>
__dict__ <attribute '__dict__' of 'Classy' objects>
__weakref__ <attribute '__weakref__' of 'Classy' objects>
__doc__ None'''