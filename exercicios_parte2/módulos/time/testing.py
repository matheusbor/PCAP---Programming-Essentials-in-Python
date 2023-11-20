import time

print(time.ctime(time.time()))
print(time.ctime())

print(time.gmtime())
print(time.localtime())

print(time.asctime())
print(time.mktime((2019, 11, 4, 14, 53, 59, 0, 308, 0)))


tempo  = time.mktime((2019, 11, 4, 14, 53, 59, 0, 308, 0))

objeto = time.gmtime(tempo)

print(time.strftime("%Y %m %d %H %M %S", objeto))

print(time.strptime("2021/07/13 15:00:00", "%Y/%m/%d %H:%M:%S"))