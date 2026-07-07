# a estrutura de dado mais fundamental em python, é a lista. Uma lista equivale a uma coleção ordenada (parecida com um array em outras linguagens, mas com funcionalidades adicionais)
integer_list = [1, 2, 3]
heterogeneous_list = ["string", 0.1, True]
list_of_lists = [integer_list, heterogeneous_list, []]

list_length = len(integer_list)   # igual a 3
list_sum = sum(integer_list)      # igual a 6

# você pode definir o elemento de um número n de uma lista usando colchetes:
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

zero = x[0]    # igual a 0, as listas são indexadas a partir de 0
one = x[1]     # igual a 1
nine = x[-1]   # igual a 9, 'pythonic', para o último elemento
eight = x[-2]  # igual a 8, 'pythonic', para o penúltimo elemento
x[0] = -1      # agora x é [-1, 1, 2, ..., 9]

#