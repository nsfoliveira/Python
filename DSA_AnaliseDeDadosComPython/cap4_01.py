
# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())

import datetime

agora = datetime.datetime.now()

print (agora)

tempo = datetime.time(7,8,12)

print (tempo)

from functools import reduce

lista = [28,35,1]

def soma(a,b):
    x = a +b
    return x

reduce(soma, lista)