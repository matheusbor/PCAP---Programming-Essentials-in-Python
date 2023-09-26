

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

def verificar2(text):
    text2 = ""
    for i in range(len(text)-1, -1, -1):
        text2 += text[i]
    return text2

def comparar(texto):
    if text == texto:
        print(palindromo,"é um palindromo")
    else:
        print("Não é um palindromo")
    
    
palindromo = input("Digite o palindromo: ")
text = tratamento(palindromo)

ask = 0
while ask != "1" and ask != "2":
    ask = input("Deseja usar qual verificação? \n 1 - Lista\n 2 - Index \n")

if ask == "1":
    if text == "":
        print("Não é um palindromo")
    else: 
        texto = verificar(text)
        comparar(texto)
    
elif ask == "2":
    if text == "":
        print("Não é um palindromo")
    else: 
        texto = verificar2(text)
        comparar(texto)
    

