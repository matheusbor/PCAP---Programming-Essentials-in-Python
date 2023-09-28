num1 = input("Digite um numero: ")
num2 = input("Digite outro numero: ")

try:
	print(num1 / num2)
	print("hello")
except ValueError:
	print("O caracter introduzido não é um numero")

except ZeroDivisionError:
	print("A divisao por 0 é invalida")

except:
	print("Não foi possivel concluir a operação")