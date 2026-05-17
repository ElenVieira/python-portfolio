for i in [1, 2, 3, 4, 5]:
    print(i)                    # primeira linha do bloco "for i"
    for j in [1, 2, 3, 4, 5]:
        print(j)                # primeira linha do bloco "for j"
        print (i + j)           # ultima linha do bloco "for j"
    print (i)                   # ultima linha do bloco "for i"
print ("done looping")    

# é muito importantante entender que o seu código não ira executar corretamente caso misture espaços e tabulação. No python sempre utilize espaços

# o espaço em branco é ignorado quando utilizado dentro de parenteses e colchetes, útil para visualização de computações intermináveis 
long_winded_computation = (1 + 2 + 3 + 4 + 5 + 5 + 7 + 8 + 9 + 10 + 11 + 12 + 13 + 14 + 15 + 16 + 17 + 18 + 19 + 20)

# para facilitar a leitura do código: 
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

easier_to_read_list_of_lists = [[1, 2, 3],
                                [4, 5, 6],
                                [7, 8, 9]]

# a formatação dos espaços em branco pode dificultar as ações de copiar e colar no sheel do python. Ex, se tentasse colar o códg abaixo no sheel comum:
# for i in [1, 2, 3, 4, 5]:

    # observe a linha em branco
    # print(i)
# apareceria a seguinte mensagem: 
# IndentationError: expected an intented block    

# e isso acontece porque o interpretador acha que a linha em branco é o fim do bloco do loop for

# DICA: o IPython tem a função %paste, que copia corretamente o conteúdo da área de transfêrencia, com os espaçoes em branco e tudo mais. Só isso já é um excelente motivo para usar o IPython.
