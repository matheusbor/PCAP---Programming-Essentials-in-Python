

line = input("Enter a line of numbers - separate them with spaces: ")
strings = line.split()

if len(strings) == 0:
    print("Nenhum valor foi inserido")
else:
    total = 0
    try:
        for substr in strings:
            total += float(substr)
        print("The total is:", total)
    except:
        print(substr, "is not a number.")
