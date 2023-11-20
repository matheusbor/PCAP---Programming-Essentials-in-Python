from datetime import datetime
objeto = datetime(2020, 11, 4, 14, 53)

print(objeto.strftime("%Y/%m/%d %H:%M:%S"))
print(objeto.strftime("%Y/%B/%d %H:%M:%S %p"))


print(objeto.strftime("%a, %Y %b %d"))

print(objeto.strftime("%A, %Y %B %d"))

print(objeto.strftime("Weekday: %w"))
print(objeto.strftime("Day of the year: %j"))
print(objeto.strftime("Week number of the year: %U"))