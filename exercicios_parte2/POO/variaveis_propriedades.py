class exemplo:
    varia = 1
    def __init__(self, val):
        exemplo.varia = val

objeto = exemplo(3)

print(exemplo.__dict__)#como a variável é usada na variável de classe, se não especificarmos que a variável é da classe ela criaria uma nova variável local

print(objeto.__dict__)# como não tem variável de instância não tem nada

print(hasattr(exemplo, 'varia'))