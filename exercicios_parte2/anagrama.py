def tratamento(text):
    text = text.upper()
    texto = ""
    for char in text:
        if char == " ":
            continue
        texto += char
    return texto
    
def verificar(text1, text2):
    if len(text1) != len(text2):
        return False
    
    list1, list2 = iterar(text1, text2)
    
    contagem = {}
    contagem2 = {}
    for elem in list1:
        if elem not in list2:
            return False
        contagem[elem] = text1.count(elem)#dicinario
    for elem in list2:
        if elem not in list1:
            return False
        contagem2[elem] = text2.count(elem)
    
    for elem in contagem.keys():
        for elemen in contagem2.keys():
            if elem == elemen:
                if contagem[elem] != contagem2[elemen]:
                    return False
    return True
                

        

def iterar(text1, text2):
    list1 = []
    for char in text1:
        if char not in list1:
            list1.append(char)
    list2 = []
    for char in text2:
        if char not in list2:
            list2.append(char)
    
    return list1, list2
    


text1 = input("Digite a primeira forma do anagrama: ")
text1 = tratamento(text1)

text2 = input("Digite a segunda forma do anagrama: ")
text2 = tratamento(text2)

if verificar(text1, text2):
    print("São anagramas")
else:
    print("Não são anagramas")
