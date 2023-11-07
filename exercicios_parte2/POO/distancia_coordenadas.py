

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__coordenada = [x, y]

    def getx(self):
        return self.__coordenada[0]

    def gety(self):
        return self.__coordenada[1]

    def distance_from_xy(self, x, y):
        #__intermediario = [x, self.__coordenada[1]]
        __a = self.__coordenada[0] - x
        __a = tratar_negativo(__a)
        
        __b = self.__coordenada[1] - y
        __b = tratar_negativo(__b)
        
        return (__a*__a + __b * __b)**0.5
        

    def distance_from_point(self, point):
        #__intermediario = [point.__coordenada[0], self.__coordenada[1]]
        __a = self.__coordenada[0] - point._Point__coordenada[0]
        __a = tratar_negativo(__a)
        
        __b = self.__coordenada[1] - point._Point__coordenada[1]
        __b = tratar_negativo(__b)
        
        return (__a*__a + __b * __b)**0.5

def tratar_negativo(x):
    if x < 0:
        return x * -1
    return x #se eu não retorno um valor para a segunda condição como eu to atribuindo, retorna implicitamente void
        
point1 = Point(0, 0)
#print(point1._Point__coordenada[0])
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))
