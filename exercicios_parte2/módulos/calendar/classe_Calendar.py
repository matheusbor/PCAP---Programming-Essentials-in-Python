import calendar


objeto = calendar.Calendar(firstweekday = 6)

for day in objeto.iterweekdays():
    print(day, end = " ")

print()
#print(list(objeto.itermonthdates(2020, 3)))

print(list(objeto.itermonthdays(2020, 3)))
#print(list(objeto.itermonthdays2(2020, 3)))
#print(list(objeto.itermonthdays3(2020, 3)))

print(objeto.monthdays2calendar(2020, 3))