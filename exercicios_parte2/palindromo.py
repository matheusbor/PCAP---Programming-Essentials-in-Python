

def tratamento(text):
    text = text.upper()
    texto = ""
    for char in text:
        if char == " ":
            continue
        texto += char
    return texto
    
    
def verificar(text):
    texto = []
    for char in text:
        texto.insert(0, char)
    texto = "".join(texto)
    return texto


def comparar():
    if text == texto:
        print(palindromo,"é um palindromo")
    else:
        print("Não é um palindromo")
    
    
palindromo = input("Digite o palindromo: ")
text = tratamento(palindromo)


if text == "":
    print("Não é um palindromo")
else: 
    texto = verificar(text)
    comparar()


