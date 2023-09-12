def mysplit(string):
    list = []
    
    if string.isspace():
        return list
    elif string == "": #"" é vazio porém pode entrar uma string vazia na lista, é um valor válido
        return list
        
    str_auxiliar = ""

    for i in string:
        
        if i.isspace():
            if len(str_auxiliar) == 0:
                continue
            
            list.append(str_auxiliar)
            str_auxiliar = ""
            continue
        else:
            str_auxiliar += i
    else: 
        list.append(str_auxiliar) #precisei colocar o else no for porque a string termina no n o que não caía no caso que tinha a inserção na lista
    return list


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
