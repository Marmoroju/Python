'''nome = str(input('Qual é o seu nome?')).strip()
if nome == 'Marcos':
    print(f'{nome}, que nome lindo você tem!')
else:
    print('Seu nome é tão normal')
print(f'Bom dia, {nome}')'''

n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
m = (n1 + n2) / 2
print(f'A sua média final foi {m:.1f}')

#condição simplificada
print('Parabéns!' if m >=6 else 'Precisa estudar mais!')

#condição normal
'''if m >= 6.0:
    print('Parabéns, a sua média foi boa!')
else:
    print('Sua média foi ruim, precisa estudar mais!')'''
