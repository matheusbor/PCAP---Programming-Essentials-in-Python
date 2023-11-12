class one:
	pass
class two:
	pass

class three(one , two):
	pass

def printar_nomes(classe):
	print("")
	for i in classe.__bases__:
	    print(i.__name__, end = " ")
    
objeto = one()
print("o nome da classe e: ", type(objeto).__name__)

print(objeto.__module__)
print(one.__module__)

printar_nomes(one)
printar_nomes(three)