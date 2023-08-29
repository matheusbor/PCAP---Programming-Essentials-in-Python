#Tentativa 1
'''
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

tempo_hora = dura //60

tempo_minuto = dura % 60
#atribuir que se minutos passarem de 60 vai incrementar 1 na hora
hour = (hour + tempo_hora) + (mins + tempo_minuto)//60

#atribuir que os minutos não podem passar de 59
mins = (mins + tempo_minuto) % 60

#atribuir que horas não podem passar de 24
hour = hour % 24

hour = str(hour)
mins = str(mins)


print("A hora que termina é: " + hour + ":" + mins )
'''


# tentativa 2

hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

#soma todos minutos 
mins += dura

#Ve quantas horas tem nos minutos
hour +=  mins//60

#formata os minutos
mins %=  60

#formata as horas
hour %=  24

hour = str(hour)
mins = str(mins)
print(type(hour))
print("A hora é: " + hour + ":" + mins)
