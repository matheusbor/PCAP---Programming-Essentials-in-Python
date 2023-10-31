class Timer:
    def __init__(self, hour = 0, minute = 0, seconds = 0):
        self.__seconds = hour * 3600 + minute * 60 + seconds
        self.__minutes
        self.__hours
    def __str__(self):
        if self._Timer.__seconds >= 3600:
            self._Timer.__hours = self._Timer.__seconds // 3600

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
