secreto = 'perfume'
digitadas = []
chances = 3

while True:
    if chances == 0:
        print('Você perde!')
        break

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

    secreto_temp = ''

    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temp += letra_secreta
        else:
            secreto_temp += '*'

    print(secreto_temp)

    if secreto_temp == secreto:
        print('Fim de jogo')
        break
    else:
        print(f'A palavra secreta está assim : {secreto_temp}')

    if letra not in secreto:
        chances -= 1