class WeekDayError(Exception):
    pass
	

class Weeker:
    week = {
        "Sun": 1,
        "Mon": 2,
        "Thu": 3,
        "Wed": 4,
        "Thu": 5,
        "Fri": 6,
        "Sat": 7
    }
    
    week2 = {
         1: "Sun",
         2: "Mon",
         3: "Thu",
         4: "Wed",
         5: "Thu",
         6: "Fri",
         7: "Sat"
    }
    
    
    def __init__(self, day):
        if day not in Weeker.week.keys():
            raise WeekDayError
        self.__day = Weeker.week[day]

    def __str__(self):
        return Weeker.week2[self.__day]#ela imprime o valor quando é chamada uma função print apenas com o objeto

    def add_days(self, n):
        temporario = n // 7
        n -= temporario * 7
        if (self.__day + n ) > 7:
            self.add_days(n)
        self.__day += n
        return self.__day
        

    def subtract_days(self, n):
        temporario = n // 7
        n -= temporario * 7
        if (self.__day - n ) > 7:
            self.subtract_days(n)
        self.__day -= n
        return self.__day


try:
    weekday = Weeker('Mon')
    print(weekday)
   
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")