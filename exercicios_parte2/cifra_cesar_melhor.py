text = input("Digite o texto: ")

desloc = 0
while(desloc not in range(1, 26)):
    desloc = int(input("Digite um valor de 1 a 25 para o deslocamento: "))
   
cifra = ""
    
for char in text:
    if not char.isalnum() or char.isdigit():
        cifra += char
    else:
        if char.isupper():
            code = ord(char) + desloc
            if code > ord("Z"):
                temp = code - (ord("Z") + 1) 
                # o 1 é por questao de limite, se a letra for z  ecomeçar a incrementar do a por exemplo e o desloc for 2 vai dar c ao inves de b, outra solução seria  colocar o caracter que tem 1 ao menos no code point do que o a 
                code = ord("A") + temp
            cifra += chr(code)
        else:
            code = ord(char) + desloc
            if code > ord("z"):
                temp = code - (ord("z") + 1)
                code = ord("a") + temp
            cifra += chr(code)
print(cifra)
        