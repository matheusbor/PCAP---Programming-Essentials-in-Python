income = float(input("Enter the annual income: "))

if income <= 85528:
    imposto = (income / 100)*18 - 556.2
elif income >= 85528:
    excesso = income -85528
    imposto = 14839.2 + 32*(excesso / 100)

if imposto < 0:
    imposto = 0.
    
tax = round(imposto, 0)
print("The tax is:", tax, "thalers")

#segunda tentativa, acho que está mais certo
#como a casa decimal é arredondada não dá para saber o certo
'''
income = float(input("Enter the annual income: "))

if income<=85528:
    tax = (income/100 * 18) - 556.02
else:
    tax = 14839.02 + ((income - 85528)/100) * 32

if tax<0:
    tax = 0.

tax = round(tax, 0)
print("The tax is:", tax, "thalers")

'''