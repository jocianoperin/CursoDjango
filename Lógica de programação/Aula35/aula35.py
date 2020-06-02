lista = ['Jociano', 'Perin']
inicia_j = False

for valor in lista:
#    if valor.startswith('J'):
#        print('Começa com J', valor)
#    else:
#        print('Não começa com J', valor)
    if valor.startswith('J'):
        inicia_j = True

if inicia_j:
    print('Existe uma palavra que inicia com J.')
else:
    print('Não existe uma palavra que começa com J.')