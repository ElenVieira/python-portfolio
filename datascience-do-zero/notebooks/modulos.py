# alguns recursos do python não são carregados por padrão, como componentes integrados à linguagem e elementos externos, disponíveis para download. Para isso é preciso importar (import) esses respectivos módulos
import re
my_regex = re.compile("[0-9]+", re.I)

# o 're' é o módulo que contém as funções e constantes aplicáveis às expressões regulares. Após esse tipo de import, para acessar as respectivas funções, você deve usar o prefixo re.
# se j´pa ouver um re no código, você pode usar um alias: 
import re as regex
my_regex = regex.compile("[0-9]+", regex.I)

# você pode fazer isso se o módulo tiver um nome muito complicado ou se precisar digitar um trecho muito longo
# ex: para visualizar os dados com o matplotlib exesite um padrão: 
import matplotlib.pyplot as plt
plt.plot(...)

# para obter valores específicos de um módulo, você pode importar o conteúdo expressamente e usá-los sem qualificação: ]
from collections import defaultdict, Counter
lookup = defaultdict(int)
my_counter = Counter
