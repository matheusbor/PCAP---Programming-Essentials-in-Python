list = [x * x for x in range(5)]
def fun(lst):
    del lst[lst[2]] #faz a recursividade da LISTA
    return lst

print(fun(list))