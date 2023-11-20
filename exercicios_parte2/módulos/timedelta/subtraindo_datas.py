from datetime import datetime
from datetime import timedelta

objeto = datetime(2023, 10, 20, 22, 50, 30)
print(objeto)

objeto2 = datetime(2020,6,10,15,40,59)
print(objeto2)

objeto3 = objeto - objeto2

print(objeto3)

objeto4 = timedelta(weeks = 52, hours= 7)
print(objeto4)