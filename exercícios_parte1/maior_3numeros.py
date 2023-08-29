num1 = int(input("Digite o numero 1 "))
num2 = int(input("Digite o numero 2 "))
num3 = int(input("digite o numero 3 "))

maior_numero = num1

if maior_numero < num2:
    maior_numero = num2
if maior_numero < num3:
    maior_numero = num3

print("O maior número é: ", maior_numero)

#ou simplismente
'''
maior_numero = max(num1, num2, num3)
print("O maior numero é: ", maior_numero)
'''