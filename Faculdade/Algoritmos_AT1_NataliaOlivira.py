'''
A Média Móvel é um estimador usado frequentemente para suavizar flutuações curtas e destacar tendências a longo prazo em
 séries temporais.
Durante a pandemia de Covid-19 a média móvel dos últimos 7 dias do número de casos e mortes causadas pelo vírus tem sido
comumente utilizada.
A Média Móvel de casos de Covid-19 nos últimos 7 dias é calculada como a média aritmética do número de casos dos últimos
7 dias.
Para auxiliar o desenvolvimento de um algoritmo para calcular a Média Móvel de casos de Covid-19 nos últimos 7 dias,
identifique:
'''

# a) Quais são os dados de entrada?

# criando  uma lista vázia
casos = []

# utilizando um loop for para povoar a lista com as entradas informadas pelo usuário
for i in range(14):
    casos.append(int(input('Qual o numero de casos: ')))

# imprimindo na tela a lista de casos
print(casos)

# B) Quais são as etapas que envolvem o processamento?

# deslocamento, no caso, serão 7  dias; variavel aux; lista que receberá as média
desloc = 7
j = 0
med_mov = []

# calculando a média móvel usando loop while
while j < len(casos) - desloc:
    calc = casos[j:j + desloc]
    med = sum(calc) / desloc
    med_mov.append(med)
    j += 1

# c) Qual é a saída do algoritmo?

print(med_mov)


