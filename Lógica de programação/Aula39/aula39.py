#operador ternário

logged_user = False

if logged_user:
    msg = 'Logado'
else:
    msg = 'Necessário logar'

print(msg)

###
logged_user = False
msg = 'Usuário logado' if logged_user else 'Usuário precisa logar'
print(msg)

###
idade = 18
if idade >= 18:
    print('Pode entrar')
else:
    print('Não pode entrar')

idade = input('Qual sua idade?')

try:
    idade = int(idade)
    maior = (idade >= 18)
    msg = 'Pode acessar' if maior else 'Não pode entrar'
    print(msg)
except ValueError as err:
    print('Digite apenas números')
    pass