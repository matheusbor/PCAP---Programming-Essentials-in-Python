lista_soma = [2, 3.14, 76, 0.5, 0.3, 2, 0.9]
historico = []
total = 0

for i in lista_soma:
    total += i
    historico.append(total)
    print("O valor atualmente é: ", total)
print("O total é: ", total)
print("Histórico das operações: ", historico)