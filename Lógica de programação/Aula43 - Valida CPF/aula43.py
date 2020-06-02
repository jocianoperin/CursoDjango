cpf = input('Digite seu CPF: ')
char = '.-'
tot = 0
tot1 = 0

for c in range(0, len(char)):
    cpf = cpf.replace(char[c], "")

while (len(cpf) != 11) or (cpf.isnumeric() == False):
    print('Digite um valor de CPF no formato correto!')
    cpf = input('Digite seu CPF: ')
else:
    print('O CPF digitado é: ', cpf)
    for p, r in enumerate(range(11, 1, -1)):
        if (p <= 8):
            tot = tot + (int(cpf[p]) * (r - 1))
            tot1 = tot1 + (int(cpf[p]) * r)
        else:
            tot1 = tot1 + (int(cpf[p]) * r)

    if (11 - (tot % 11) > 9):
        dig1 = 0
    else: dig1 = 1

    dig2 = 11 - (tot1 % 11)

    #print(dig1, dig2, cpf[-2], cpf[-1])

    if(dig1 == int(cpf[-2]) and dig2 == int(cpf[-1])):
        print('CPF válido')
    else:
        print('CPF não é válido')