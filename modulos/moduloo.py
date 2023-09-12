print("TEste do módulo")

contadora = 0

def soma(lista):
    global contadora
    contadora += 1
    soma = 0
    for i in lista:
        soma += i
    return soma

