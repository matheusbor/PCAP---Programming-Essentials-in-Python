def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True
        

def days_in_month(year, month):
    if month > 12:
        return None
    duration_months= ["o codigo de teste tava errado", 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_year_leap(year):
        duration_months[2] = 29
    return duration_months[month]

def day_of_year(year, month, day):
    if day > 31:
        return None
    days_count = 0
    for i in range (1, month):#nao precisa de month + 1 pois o dia já conta os dias do ultimo mes
        days_count += days_in_month(year, i)#nao soma a string que esta na 0 posição
    days_count += day
    return days_count
    

test_years = [2000, 1900, 2000, 2016, 1987]
test_months = [12, 12, 2, 1, 11]
test_days = [31, 31, 15, 23, 30]

for i in range(len(test_years)):
    print(day_of_year(test_years[i], test_months[i], test_days[i]))

