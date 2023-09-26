palavra = input("Digite uma palavra: ")

frase = input("Digite a frase: ")
#frase = "abcdefghijklmnopqrstuvxwyz"

posicao = -len(frase)#porque precisava de um index negativo para ser incluido o começo
verificador =0
for char in palavra:
    pos_temp = posicao
    #if palavra.index(char) == palavra.find:#verificar se a palavra foi encontrada, pois se não for index retorna nada e find -1
    #sem alguma forma de tratar o erro não funciona
    posicao = frase.find(char, posicao )#se isso aqui der certo executa isso aqui

    #print(pos_temp, posicao)
    if posicao == -1:
        print(char, "não encontrada")
    elif posicao != pos_temp:
        print(char, "encontrada")
        verificador += 1
        
if verificador == len(palavra):
    print("Palavra encontrada")
else:
    print("Palavra não encontrada")
    