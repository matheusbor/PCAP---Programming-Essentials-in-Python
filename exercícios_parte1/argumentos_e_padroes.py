def registro(idade, altura, genero, civil = 'solteiro'):
    print("Oi", genero, 'de', altura, 'com', idade, 'anos', 'que ta', civil)

age = input("Digite sua idade: ")
gender = input("Digite seu genero: ")
height = input("Digite sua altura: ")

registro(age, genero = gender, altura = height)