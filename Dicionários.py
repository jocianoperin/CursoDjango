d1 = dict(chave1='Valor da chave1', chave2='Valor da chave2')

if 'chave2' in d1:
    print (d1['chave2'])
else:
    print('Não existe')

d1.update({'chave2':'novo valor'})

print(d1)