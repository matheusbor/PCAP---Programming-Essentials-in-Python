import os

os.chdir("exercicios_parte2/módulos")
'''comandos usados para criação

os.mkdir("tree")

os.chdir("tree")
#os.chdir("c")
#os.chdir("other_courses")

os.mkdir("c")
os.mkdir("cpp")
os.system("mkdir python")

os.makedirs("other_courses/cpp")
os.mkdir("python")

os.makedirs("cpp/other_courses/c")
os.makedirs("cpp/other_courses/python")

os.makedirs("python/other_couses/c")
os.makedirs("python/other_couses/python")
os.rmdir("C:\\Users\\mathe\\Desktop\\vscode\\Github\\netacad\\exercicios_parte2\\módulos\\tree\\python\\other_couses\\python")
os.makedirs("python/other_couses/cpp")


'''


def find(path = "./", dir = "", recursao = False):
    if recursao:
        os.chdir(path)
        os.chdir("../")
    else:
        os.chdir(path)
    #print("caminho", os.getcwd())
    arquivos = os.listdir()

    if dir in arquivos:
        os.chdir(dir)
        path = os.getcwd()
        os.chdir("C:\\Users\\mathe\\Desktop\\vscode\\Github\\netacad\\exercicios_parte2\\módulos")#precisa voltar o caminho
        return path
    else:
        return find(str(os.getcwd()), dir, True)


print(find("tree\cpp\other_courses\c", "cpp"))

print(find("./tree", "python"))