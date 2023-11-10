class SoftwareError(Exception):
    def __init__(self, requisições = 0, status = True, message = "Houve um erro no Software"):
        Exception.__init__(self, message)
        self.status = status

class TooMuchRequisições(SoftwareError):
    def __init__(self, requisições = 100, message = "Temos muitas requisições no momento, tente novamente mais tarde"):
        SoftwareError.__init__(self, requisições = requisições, message = message)
        self.requisições = requisições

def conectar_servidor(status, requisições):
    if requisições >= 100:
        raise TooMuchRequisições(requisições = requisições)
    if status == False:
        raise SoftwareError(status = status)
    print("Você está conectado")
   
for (stts, requisitions) in [(True, 50), (False, 101), (False, 99)]:
    try:
        conectar_servidor(stts, requisitions)
    except TooMuchRequisições as TMR:
        print("Desculpe, ", TMR)
    except SoftwareError as SW:
        print("Desculpe, ", SW)


