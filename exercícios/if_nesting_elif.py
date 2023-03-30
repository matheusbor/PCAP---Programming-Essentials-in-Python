lapis_azul = int(input("quantos lapis azuis voce tem "))
lapis_vermelho = int(input("quantos lapis vermelhos voce tem "))
lapis_amarelo = int(input("quantos lapis amarelos vc tem "))

if lapis_azul==True:
    print("desenhar mar")

if lapis_azul&lapis_vermelho==True:
    print("desenhar o por do sol")
else:
    print("não temos lapis de cor suficientes")

if lapis_amarelo==True:
    print("desenhar por do sol na praia")
elif lapis_azul&lapis_vermelho==True:
    print("desenhar o por do sol")
else:
    print("não temos lapis de cor suficientes")
