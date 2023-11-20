from datetime import date
from time import time 

segundos = time()

data_atual = date.fromtimestamp(segundos)

print(data_atual)