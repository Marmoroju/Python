nome = str(input('Digite aqui o seu nome:'))
if nome == 'Marcos':
    print('Que nome lindo você tem!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'José':
    print('Que nome popular você tem!')
elif nome in 'Ana Julia Marcela Martha':
    print('O seu nome é bem popular no Brasil.')
else:
    print('Que nome comum o seu.')
print(f'Tenha um bom dia, {nome}!')