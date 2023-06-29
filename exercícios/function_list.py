def multiplicação(lista):
	multi = 1
	for elemento in lista:
		multi *= elemento
	return multi

print(multiplicação([x for x in range(1, 20)]))