
def somar(data):
    soma = 0
    for char in data:
        soma += int(char)
    while soma / 10 >= 1:
        data = str(soma)
        soma = somar(data)
    return soma


data = input("Digite a data do seu nascimento no formato DDMMAAAA: ")

print("O digito é: ",somar(data))
        
    