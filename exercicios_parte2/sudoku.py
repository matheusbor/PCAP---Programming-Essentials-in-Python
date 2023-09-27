tabuleiro = [[" " for i in range(9)] for i in range(9)]


'''
tab_test = [[" " for i in range(9)] for i in range(9)]
tab_test[0] = "295743861"
tab_test[1] = "431865927"
tab_test[2] = "876192543"
tab_test[3] = "387459216"
tab_test[4] = "612387495"
tab_test[5] = "549216738"
tab_test[6] = "763524189"
tab_test[7] = "928671354"
tab_test[8] = "154938672"
'''

def ler():
    for i in range(9):
        linha = input("Digite uma linha de números: ")
        #linha = tab_test[i]
        for j in range(len(linha)):
            tabuleiro[i][j] = linha[j]

def regioes():
    registra = []
    contador = 1
    adicionados = 0
    linha = 0
    coluna = 0
    for i in range(1, 10):#se o loop tem muita condicao é mais facil usar condicoes do que vários loops com index automaticos
        if i < 4:
            linha = 0
        elif i < 7:
            linha = 3
        elif i < 10:
            linha = 6
        if i > 1:
            contador += 1
        if i == 4 or i == 7:
            contador = 1
        for linha in range(linha, linha + 3):#a ordem dos for é a ordem decrescente de como o tabuleiro vai ser varrido
            if contador == 1:
                coluna = 0
            elif contador == 2:
                coluna = 3
            elif contador == 3:
                coluna = 6
            for coluna in range(coluna, coluna + 3):#preciso de uma forma de incrementar isso varias vezes
                if adicionados == 9:
                    registra = []
                    adicionados = 0
                if tabuleiro[linha][coluna] not in registra:#criar um index que se auto incrementa e so analisa a regiao 3x3
                    registra.append(tabuleiro[linha][coluna])
                    adicionados += 1
                else:
                    print("Numero repetido no quadrado")
                    return False
                
    return True

def linha():
    registra = []
    for linha in range(9):
        for coluna in range(9):
            if tabuleiro[linha][coluna] not in registra:
                registra.append(tabuleiro[linha][coluna])
            else: 
                print("Número repetido na linha")
                return False
        #print(registra)
        registra = []
    return True

def coluna():
    registra = []
    for coluna in range(9):
        for linha in range(9):
            if tabuleiro[linha][coluna] not in registra:
                registra.append(tabuleiro[linha][coluna])
            else: 
                print("Número repetido na coluna")
                return False
        
        #print(registra)
        registra = []
    return True


ler()

for i in range(9):
    print(tabuleiro[i])

if regioes() and linha() and coluna():
    print("O sudoku é válido")
else:
    print("O sudoku não é valido")


