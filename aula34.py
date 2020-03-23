secreto = 'perfume'
digitadas = []

while True:
    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Digite apenas uma letra!')
        continue

    digitadas.append(letra)

    print(digitadas)

    if letra in secreto:
        print(f'A letra "{letra}" existe na palavra secreta.')

    else:
        print(f'A letra "{letra}" não existe na palvra secreta.')