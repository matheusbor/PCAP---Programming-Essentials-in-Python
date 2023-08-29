n = int(input("Digite ate onde vai a sequencia: "))

def fibonacci(n):
    fib1 = 1
    fib2 = 1
    print(fib1)
    print(fib2)
    for i in range(n - 2):
        fib = fib1 + fib2
        fib1, fib2 = fib2, fib
        print(fib)

fibonacci(n)