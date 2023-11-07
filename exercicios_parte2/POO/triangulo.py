import math


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
        __a = self.__coordenada[0] - point.__coordenada[0]
        __a = tratar_negativo(__a)
        
        __b = self.__coordenada[1] - point.__coordenada[1]
        __b = tratar_negativo(__b)
        
        return (__a*__a + __b * __b)**0.5


def tratar_negativo(x):
    if x < 0:
        return x * -1
    return x 


class Triangle(Point):
    def __init__(self, vertice1, vertice2, vertice3):
        Point.__init__(self)
        
        self.__primeiro_ponto = vertice1._Point__coordenada[:]
        self.__segundo_ponto = vertice2._Point__coordenada[:]
        self.__terceiro_ponto = vertice3._Point__coordenada[:]
        

    def perimeter(self):
        ponto = Point(self.__primeiro_ponto[0], self.__primeiro_ponto[1])
        a = ponto.distance_from_xy(self.__segundo_ponto[0], self.__segundo_ponto[1])
        #o método distance from point está configurado para acessar a lista de um objeto não apenas uma lista
        c = ponto.distance_from_xy(self.__terceiro_ponto[0], self.__terceiro_ponto[1])
        
        ponto2 = Point(self.__segundo_ponto[0], self.__segundo_ponto[1])
        b = ponto2.distance_from_xy(self.__terceiro_ponto[0], self.__terceiro_ponto[1])
        
        return a + b + c

triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
