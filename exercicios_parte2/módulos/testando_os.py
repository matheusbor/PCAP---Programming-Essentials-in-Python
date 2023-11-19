import os

#print(os.uname())

print(os.name)

#os.mkdir(path = "exercicios_parte2\\módulos\\teste\\teste")

#os.makedirs("teste/teste/teste1/teste2")
#os.chdir("exercicios_parte2\módulos/teste/teste")
print("caminho", os.getcwd())
print(os.listdir())
#os.rmdir("teste/teste/teste1/teste2")
#os.chdir("exercicios_parte2/módulos/teste/teste/")


#os.mkdir("ola_teste")
#os.makedirs("ola_teste/oiteste/uauteste")
print(os.listdir())

#os.rmdir("ola_teste")
#os.removedirs("teste/teste/teste1")
#os.removedirs("ola_teste/oiteste/uauteste")

#os.chdir("exercicios_parte2/módulos")
#os.removedirs("teste/teste1")
retorno = os.system("mkdir exercicios_parte2\\módulos\\teste\\teste1")
print(retorno)

os.chdir("../")
print(os.getcwd())