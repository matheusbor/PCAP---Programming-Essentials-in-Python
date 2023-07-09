def bmi(weight, height):
    if height < 1.0 or height > 2.5 or \
    weight < 20 or weight > 200:
        return None

    return weight / height ** 2

def lb_to_kg(lb):
    return lb * 0.45359237
    
def ft_and_inch_to_m(ft, inch = 0.0):#nao da pra usar in pq é keyword
    altura = ft * 0.3048 + inch * 0.0254
    return altura #podia ter sido feito direto no return
    
print(bmi(352.5, 1.65))
print(bmi(lb_to_kg(176), 1.75))
