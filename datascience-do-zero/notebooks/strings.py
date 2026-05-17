# as strings podem ser delimitadas por aspas simples ou duplas (mas sempre combinando):
single_quoted_string = 'data science'
double_quoted_string = "data science"

# no python a barra invertida serve para codificar caracterers especiais. Por exemplo:
tab_string = "\t"   # representa o caractere tab
len(tab_string)     # o tamanho é 1

#para usar o caractere da barra invertida (como vemos nos nomes dos diretórios e nas expressões regulares do windows), você pode criar strings brutas com r"":
not_tab_string = r"\t"  # representa o caractere tab
len(not_tab_string)     # o tamanho é 2