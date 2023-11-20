from datetime import datetime, time

objeto = datetime(2023, 11, 20, 12, 00 )
print(objeto)

print(datetime.today())
print(datetime.now())
print(datetime.utcnow())

print(objeto.timestamp())

print(objeto.strftime("%d do %m de %Y"))


t = time()
print(t.strftime("%Y %m %d %H %M %S"))

print(datetime.strptime("2021/07/13 15:00:00", "%Y/%m/%d %H:%M:%S"))
