from os import strerror

modifica = open("exercicios_parte2/manipulação_arquivos/zen_do_python.txt", "wt", encoding="utf-8")

for i in range(50):
    modifica.write("Hello, World!\n")


modifica.close()

ler = open("exercicios_parte2\\manipulação_arquivos\\zen_do_python.txt", "r", encoding= "utf-8")
for i in ler:
    print(i)
print(modifica)



'''modifica.write(- O Zen do Python é uma coleção de princípios, para escrever programas de computador que influenciam o design da linguagem de programação Python.
    - Bonito é melhor que feio.
    - Explícito é melhor que implícito.
    - Simples é melhor que complexo.
    - Complexo é melhor que complicado.
    - Plano é melhor que aglomerado.
    - Esparso é melhor que denso.
    - Legibilidade faz diferença.
    - Casos especiais não são especiais o bastante para quebrar as regras.
    - Embora a praticidade vença a pureza.
    - Erros nunca devem passar silenciosamente.
    - A menos que sejam explicitamente silenciados.
    - Diante da ambigüidade, recuse a tentação de adivinhar.
    - Deve haver um - e preferencialmente só um - modo óbvio para fazer algo.
    - Embora esse modo possa não ser óbvio à primeira vista a menos que você seja holandês.
    - Agora é melhor que nunca.
    - Embora nunca freqüentemente seja melhor que *exatamente* agora.
    - Se a implementação é difícil de explicar, é uma má idéia.
    - Se a implementação é fácil de explicar, pode ser uma boa idéia.
    - Namespaces são uma grande idéia -- vamos fazer mais dessas!)'''