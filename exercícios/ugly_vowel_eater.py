# Prompt the user to enter a word
# and assign it to the user_word variable.
user_word = input("Escreva a palavra pro vowel eater")
user_word = user_word.upper()

for letter in user_word:
    # notar que mesmo eu não tendo indicado a posição no array da string a comparação deu certo
    #ou seja a variavel incrementadora tem alguma relação com a variável "limite" que relacionam seus valores
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    print(letter)