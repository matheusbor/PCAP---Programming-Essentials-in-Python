secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
player = int(input("Digite o número secreto"))
while player != secret_number:
    if player != secret_number:
        print("vc está preso no loop")
        player = int(input("Digite o número secreto"))
print("""
Você
está
Livre
""")

pass 

#ou um mais compacto
'''
secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

number = int(input("Digite um número"))

while number != secret_number:
    print("Ha ha! You're stuck in my loop!")
    number = int(input("Digite outro número"))
    
print("O número secreto é: ", number, "Well done, muggle! You are free now.")
'''