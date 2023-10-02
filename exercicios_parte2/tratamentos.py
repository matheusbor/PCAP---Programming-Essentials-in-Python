def read_int(prompt, min, max):
    number = input(prompt)
    number = tratamento_int(number, prompt)
    #isso poderia ser substituido com um simples while// poderia mesmo?
    #teria que ser um loop dentro do outro e toda vez que for colocar uma nova condição ia criar um novo loop dentro dos loops
    number = tratamento_range(number, prompt)#tenho que declarar o prompt porque mesmo a chamada estando dentro do escopo da função quando eu vou usar na função específica não tem
    
    return number

def tratamento_int(number, prompt): 
    try:
        number = int(number)
        assert number != int#com a condição eu crio a exceção que eu quiser
        #por que o resultado dessa compração é trocada?
        return number
    except (AssertionError, ValueError):
        print("Error: wrong input")
        number = input(prompt)
        number = tratamento_int(number, prompt)
        return number
        
def tratamento_range(number, prompt):
    try:
        assert number >= -10 and number <= 10
        return number
    except AssertionError:
        print("Error: the value is not within permitted range (-10..10)")
        number = (input(prompt))
        number = tratamento_int(number, prompt)
        number = tratamento_range(number, prompt)
        return number#posso colocar aqui pois so vai chegar aqui quando o número for valido

v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
