# função é uma regra que recebe 0 ou mais entradas e retorna a saída correspondente. No python se utiliza def
def double(x):
    """
    nesse ponto, você coloca um docstring opcional para descrever a função. Por ex: Essa função multiplica a entrada por 2
    """ # docstring é como um comentário multilinha 
    return x * 2

def aplly_to_one(f):
    """chama a função f usando 1 como argumento"""
    return f(1)

my_double = double           # refere-se a função x já definida 
x = aplly_to_one(my_double)  # igual a 2

# também é fácil criar várias funções anônimas, as lambdas: 
y = aplly_to_one(lambda x: x + 4) # igual a 5

# você pode atribuir lambdas a váriasveis, embora quase todo mundo recomende o def: 
another_double = lambda x: 2 * x # não faça isso

def another_double(x):
    """faça isso"""
    return 2 * x

# os parâmetros da função também podem receber argumentos padrão, que devem ser especificados se você quiser obter um valor diferente do padrão: 
def my_print(message = "my default message"):
    print(message)

my_print("Hello")    # imprime 'hello'
my_print()           # imprime 'my default message'

# as vezes é útil especificar argumentos pelo nome: 
def full_name(first = "what is her name", last = "something"):
    return first + " " + last

full_name("Elen", "Vieira") # "Elen Vieira"
full_name("Elen")           # "Elen Something"
full_name(last = "Vieira")  # "What is her name Vieira"