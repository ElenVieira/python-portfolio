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

# você pode usar os colchetes para fatiar as listas. 
# A fatia i:j contém todos os elementos de i (incluído) a j (não incluído). 
# Se o início da fatia não for indicado, ela começará no inciio da lista; se o final não for indicado, ela terminará no final da lista.

first_three = x[:3]                 # [-1, ,1 ,2]
three_to_end = x[3:]                # [3, 4, ..., 9]
one_to_four = x[1:5]                # [1, 2, 3, 4]
last_three = x[-3:]                 # [7, 8, 9]
without_fist_and_last = x[1: -1]    #[1, 2, ..., 8]
copy_of_x = x[:]

# do mesmo modeo, você pode fatiar strings e outros tipos de 'sequências'
# a fatia pode receber um terceiro argumento para indicar seu stride, que pode ser negativo:
every_third = x[::3]        #[-1, 3, 6, 9]
five_to_three = x[5:2:-1]   #[5, 4, 3]

# o python dispõe de um operador in para veruificar a associação à lista:
1 in [1, 2, 3] # true
0 in [1, 2, 3] # false
# como essa verificação acessa todos os elementos da lista, utilize-a apenas se na lista for pequena, ou se tempo não for um problema.

# é facil concatenar listas; para modificar uma, você pode usar o extend e adicionar itens de outra coleção: 
x = [1, 2, 3]
x.extend([4, 5, 6]) # x agora é [1, 2, 3, 4, 5, 6]

# se não quiser modificar X, você pode utilizar adição de listas
x = [1, 2, 3]
y = x + [4, 5, 6]   # y agora é [1, 2, 3, 4, 5, 6], x não mudou

# na maioria das vezes, acrescentaremos item por item às listas
x = [1, 2, 3]
x.append(0)     # x agora é [1, 2, 3, 0]
y = x[-1]       # igual a 0
z = len(x)      # igual a 4

# muitas vezes é conveniente descompactar as listas quando sabemos quantos elementos elas contém
x, y = [1, 2]   # agora x é 1, Y é 2

# no entanto, aparecera um valueError se não houver o mesmo número de elementos nos dois lados.
# geralmente usamos um sublinhado para indicar o valor que será descartado
_, = [1, 2]     # agora y == 2, não considerou o primeiro elemento