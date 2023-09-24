# criptografando
def criptografar(text):
    cipher = ''
    for char in text:
        if not char.isalpha():
            continue
        char = char.upper()
        code = ord(char) + 1
        if code > ord('Z'):
            code = ord('A')
        cipher += chr(code)

    print(cipher)

def descriptografar(cipher):
    text = ''
    for char in cipher:
        if not char.isalpha():
            continue
        char = char.upper()
        code = ord(char) - 1
        if code < ord('A'):
            code = ord('Z')
        text += chr(code)

    print(text)

criptografar(input("Enter your message: "))
descriptografar(input("Digite a cifra: "))