'''
O plano diretor de desenvolvimento urbano de uma cidade determina qual
é o percentual de área máximo destinado para garagem em relação à área
total do terreno da casa, dependendo da localização desse terreno na cidade:

    Para a zona norte da cidade, o percentual máximo é de 25%.
    Para as zonas leste e oeste da cidade, o percentual máximo é de 30%.
    Para a zona sul, menos povoada, o percentual máximo é de 40%.

Uma empresa de arquitetura está com vários contratos e necessita calcular
rapidamente esse percentual, antes de iniciar os projetos. Faça um programa
que recebe as medidas do terreno e da garagem e a zona onde estará localizado
o imóvel, calcula o percentual de ocupação da área da garagem em relação
ao terreno e emite mensagem sobre o atendimento às regras de ocupação
conforme o plano diretor
'''

# Entradas
largura_garagem = float(input('Informe a largura da garagem: '))
prof_garagem = float(input('Informe a profundidade da garagem: '))
largura_terreno = float(input('Informe a largura do terreno: '))
prof_terreno = float(input('Informe a profundidade do terreno: '))
zona = input('Informar a zona onde se localiza o imóvel: S - sul; N - norte; L - leste e O - oste: ')

# Cálculos
area_garagem = largura_garagem * prof_garagem
area_terreno = largura_terreno * prof_terreno
percentual = (area_garagem/area_terreno) * 100

# resumo 1
print('Imóvel localizado na zona: ', zona)
print(f'Percentual de ocupação: {percentual:.2f}%')

# Utilizando condicional

if zona == 'N' and percentual <= 25:
    print("O projeto atende a norma de zoneamento do plano diretor")
elif zona == 'L' or 'O' and percentual <= 30:
    print("O projeto atende a norma de zoneamento do plano diretor")
elif zona =='S' and percentual <= 40:
    print("O projeto atende a norma de zoneamento do plano diretor")
elese:\
    print("REVISAR MEDIDAS. O projeto NÃO atende norma de zoneamento do plano diretor")


