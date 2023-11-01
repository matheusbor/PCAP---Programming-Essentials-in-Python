class Timer:
    def __init__(self, hour = 0, minute = 0, seconds = 0):
        self.__seconds = hour * 3600 + minute * 60 + seconds
        self.__minutes
        self.__hours
    def __str__(self):
        if self._Timer.__seconds >= 3600:
            self._Timer.__hours = self._Timer.__seconds // 3600
            self._Timer.__seconds -= self._Timer.__hours * 3600
        elif self._Timer.__seconds >= 60:
            self._Timer.__minutes = self._Timer.__seconds // 60
            self._Timer.__seconds -= self._Timer.__minutes * 60
        
        if self._Timer.__hours < 10:
            self._Timer.__hours = "0" + str(self._Timer.__hours)
        
        return self._Timer.__hours + ":" + str(self._Timer.__minutes) + ":" + str(self._Timer.__seconds)

    def next_second(self):
        #
        # Write code here
        #

    def prev_second(self):
        #
        # Write code here
        #


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
