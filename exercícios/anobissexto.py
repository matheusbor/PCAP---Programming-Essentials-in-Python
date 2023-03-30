year = int(input("Enter a year: "))

if year < 1582:
    print("Not within the gregorian calendar period")
else:
    if year % 4 != 0:
        resultado = "Common Year"
    elif year % 100 != 0:
        resultado ="Leap year"
    elif year % 400 != 0:
        resultado = "Common year"
    else:
        resultado = "Leap year"
    print("the year is a " +resultado)


#segunda tentativa
'''
year = int(input("Enter a year: "))

if year >= 1582:
    if year % 4 != 0:
        year = 'Common year'
    elif year % 100 != 0:
        year = 'Leap year'
    elif year % 400 != 0:
        year = 'Common year'
    else:
        year = 'Leap year'
else:
    print("Not within the Gregorian calendar period")
print(year)
'''