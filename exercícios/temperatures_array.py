temperatures = [[0.1 for hora in range(24)]for day in range(31)]

soma = 0.0

for dia in temperatures:
    soma += dia[12]
    
average = soma/31

temperatures [15][12] = 17.2

print("average temperature at midday/noon: ",average)

highest = -1000.0

for dia in temperatures:
    for hora in dia:
        if hora > highest:
            highest = hora
            print(highest)
print("The bigger temperature is: ", highest)

cold_days = 0

for dia in temperatures:
    if dia[12] < 15.0:
        cold_days += 1

print("The number of days that had cold temperatures at noon is: ", cold_days)
