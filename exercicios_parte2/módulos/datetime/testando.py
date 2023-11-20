from datetime import date, time
import time as t

atual = date.today()
tempo = time(23, 59, 59, 99999)
print(atual)

data = date(2023, 12, 12)

iso_data = date.fromisoformat("2020-06-06")
print(data)
print(iso_data)

data1 = data.replace(year = 2024)
print(data)
print(data1)

print(data1.weekday())
print(data1.isoweekday())
print(tempo)
t.sleep(10)
print("acordei")