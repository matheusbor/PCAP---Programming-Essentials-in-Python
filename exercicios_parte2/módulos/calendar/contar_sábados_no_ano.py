from calendar import Calendar

class MyCalendar(Calendar):
    def __init__(self):
        Calendar.__init__(self)
        self.__week_day_count = 0
        
    def count_weekday_in_year(self, ano, week_day):
        for mes in range(1, 13):
            for semana in self.monthdays2calendar(ano, mes):
                for dia in semana:
                    if dia[0] != 0:
                        if week_day == dia[1]:
                            self.__week_day_count += 1
        temp = self.__week_day_count
        self.__week_day_count = 0
        return temp

objeto = MyCalendar()

print("Quantas segundas teve em 2019? ", objeto.count_weekday_in_year(2019,0))
print("Quantos domingos teve em 2000? ", objeto.count_weekday_in_year(2000,6))