class Timer:
    __temporario = 0
    def __init__(self, hour = 0, minute = 0, seconds = 0):
        self.__seconds = hour * 3600 + minute * 60 + seconds
        self.__minutes = 0
        self.__hours = 0
    def __str__(self):
        if self.__seconds < 0:
            __temporario = ((self.__seconds) * -1)//60
            self.__seconds += __temporario * 60
            if __temporario < 1:
                __temporario = 1
            self.__minutes -=  __temporario
            self.__seconds = 60 + self.__seconds
        if self.__seconds >= 60:
            __temporario = self.__seconds // 60 
            self.__minutes += __temporario
            self.__seconds -= __temporario * 60
        
        if self.__minutes < 0:
            __temporario = ((self.__minutes) * -1)//60
            self.__minutes += __temporario * 60
            if __temporario < 1:
                __temporario = 1
            self.__hours -=  __temporario
            self.__minutes = 60 + self.__minutes
        if self.__minutes >= 60:
            __temporario  = self.__minutes // 60
            self.__hours += __temporario
            self.__minutes -= __temporario * 60

        if self.__hours < 0:
            self.__hours = 24 + self.__hours
        if self.__hours == 24:
            self.__hours = 0
        if self.__hours > 24:
            self.__hours -= 25 #pois começa do 0

        return formata(self.__hours, self.__minutes, self.__seconds)
    def next_second(self, val):
        self.__seconds += val
        self.__str__

    def prev_second(self, val):
        self.__seconds -= val
        self.__str__

    def next_minute(self, val):
        self.__minutes += val
        self.__str__

    def prev_minute(self, val):
        self.__minutes -= val
        self.__str__

    def next_hour(self, val):
        self.__hours += val
        self.__str__

    def prev_hour(self, val):
        self.__hours -= val
        self.__str__
        
  
def formata(hours, minutes, seconds):
    lista = [hours, minutes, seconds]

    for i in range(len(lista)):
        lista[i] = str(lista[i])
        if int(lista[i]) < 10:
            lista[i] = "0" + lista[i]

    return lista[0] + ":" + lista[1] + ":" + lista[2]


timer = Timer(23, 59, 59)
print(timer)

for x in range (6):
    escolha = int(input("Deseja avançar ou voltar no tempo? \nDigite 1 para avançar e 2 para voltar: "))
    print()
    if escolha == 1:
        escolha = int(input("Deseja avançar segundos, minutos, ou horas? \nDigite 1 para segundos, 2 para minutos e 3 para horas: "))
        print()
        if escolha == 1:
            timer.next_second(int(input("Quantos segundos deseja avançar: ")))
            print()
        elif escolha == 2:
            timer.next_minute(int(input("Quantos minutos deseja avançar: ")))
            print()
        elif escolha == 3:
            timer.next_hour(int(input("Quantas horas deseja avançar: ")))
            print()
    elif escolha == 2:
        escolha = int(input("Deseja voltar segundos, minutos, ou horas? \nDigite 1 para segundos, 2 para minutos e 3 para horas: "))
        print()
        if escolha == 1:
            timer.prev_second(int(input("Quantos segundos deseja voltar: ")))
            print()
        elif escolha == 2:
            timer.prev_minute(int(input("Quantos minutos deseja voltar: ")))
            print()
        elif escolha == 3:
            timer.prev_hour(int(input("Quantas horas deseja voltar: ")))
            print()
    print(timer)


