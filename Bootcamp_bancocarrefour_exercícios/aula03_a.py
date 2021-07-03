a = input('Primeiro valor: ')
b = input('Segundo valor: ')
c = input('Terceiro valor: ')

if (a > b) and (a  > c):
    print('O maior numero é: {}'.format(a))
elif (b > a) and (b > c):
    print('O maior numero é {}'.format(b))
else:
    print('O maior numero é {}'. format(c))
print('Fim do Programa')

