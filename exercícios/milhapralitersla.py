def liters_100km_to_miles_gallon(liters):
    galao = liters / 3.785411784
    milha = 62.1371
    mpg = milha / galao
    return mpg
    

def miles_gallon_to_liters_100km(miles):
    galao = (3.785411784) * 100 #como aqui medimos o comustivel consumido em 100km e nao um galao
    km = 1.609344 * miles
    liters = galao / km
    return liters
    

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
'''

def liters_100km_to_miles_gallon(liters):
    litros = liters
    galao = litros / 3.785411784
    milhas = 62.1371
    miles_gallon = milhas / galao
    
    return miles_gallon
    
    

def miles_gallon_to_liters_100km(miles):
    milhas = 3.785411784 * miles
    galao = milhas / miles
    litros = galao * 3.785411784
    km = 1.609344 * milhas
    liters = (litros / km)* 100 #n faço a menor ideia pq isso aqui funciona
    return liters 

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))

'''