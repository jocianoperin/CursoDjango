name = input('Digite o nome: ')

if name:
    print(name)
else:
    print('você não digitou nada')

print(name or 'você não digitou nada')