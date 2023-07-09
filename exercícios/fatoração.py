def entrada():
    x = int(input("Digite o numero a ser calculado o fatorial: "))
    return x
    
def factorial_function(n):
    if n < 0:
        return None

    product = 1
    for i in range(1, n + 1):
        product *= i
        
    return product


print( factorial_function(entrada()))

