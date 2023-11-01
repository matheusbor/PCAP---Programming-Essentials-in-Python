class Timer:
    def __init__(self, hour = 0, minute = 0, seconds = 0):
        self.__seconds = hour * 3600 + minute * 60 + seconds
        self.__minutes = 0
        self.__hours = 0
    def __str__(self):
        if self.__seconds >= 3600:
            self.__hours = self.__seconds // 3600
            self.__seconds -= self.__hours * 3600
        elif self.__seconds >= 60:
            self.__minutes = self.__seconds // 60
            self.__seconds -= self.__minutes * 60
        
        if self.__hours < 10:
            return "0" + str(self.__hours) + ":" + str(self.__minutes) + ":" + str(self.__seconds)
        return str(self.__hours) + ":" + str(self.__minutes) + ":" + str(self.__seconds)
    def next_second(self):
        self.__seconds += 1
        self.__str__

    def prev_second(self):
        self.__seconds -= 1
        self.__str__


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
