def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b


def entrada():
    x = float(input("DIgite um lado: "))
    return x
    
def is_right_triangle(a, b, c):
    if not is_a_triangle(a,b,c):
        return False # se nao for um triangulo vai entrar no if e retornar falso
    if a > b and a > c:
        return a**2 == b**2 + c**2 #verifica se a condição pra ser um triangulo right é verdadeira
    if b > a and b > c:
        return b**2 == a**2 + c**2
    if c > a and c > b:
        return c**2 == a**2 + b**2

print(is_right_triangle(3, 4, 5))
print(is_right_triangle(1, 3, 4)) 