# as strings podem ser delimitadas por aspas simples ou duplas (mas sempre combinando):
single_quoted_string = 'data science'
double_quoted_string = "data science"

# no python a barra invertida serve para codificar caracterers especiais. Por exemplo:
tab_string = "\t"   # representa o caractere tab
len(tab_string)     # o tamanho é 1

# para usar o caractere da barra invertida (como vemos nos nomes dos diretórios e nas expressões regulares do windows), você pode criar strings brutas com r"":
not_tab_string = r"\t"  # representa o caractere tab
len(not_tab_string)     # o tamanho é 2

# para criar strings de várias linhas use três aspas duplas
multi_line_string = """Esta é a primeira linha.
e esta é a segunda linha
e esta  é a terceira linha"""

# decarando as váriaveis
first_name = "Joel"
last_name = "Grus"

# formas de construir uma string full_name
full_name1 = first_name + " " + last_name             # adição de string
full_name2 = "{0} {1}".format(first_name, last_name)  # string.format

# f-string, forma simples de substituir valores nas strings
full_name3 = f"{first_name} {last_name}"
