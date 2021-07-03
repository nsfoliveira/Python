a = int(input('Entre com os valores: '))
b = int(input('Entre com os valores: '))
soma = a + b
subtração = a - b
multiplicação = a * b
divisão = a / b
resto = a % b

print(soma)
print(subtração)
print(multiplicação)
print(divisão)
print(resto)
print(type(soma)) #type função para retornar o tipo da variável
print('soma: {}. subtração: {}'.format(soma, subtração)) #ele consegue concatenar independente do formato.
