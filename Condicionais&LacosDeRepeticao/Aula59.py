"""  Laço de repetição 'While' """


senhaDigitada = int(input('Digite a sua senha: '))
senha = 456
if senha == senhaDigitada :
    print("Acesso permitido")
else:
    print("Acesso negado")
    while senha != senhaDigitada:
        senhaDigitada = int(input('Digite a sua senha: '))
        senha = 456
    if senha == senhaDigitada :
        print("Acesso permitido")
    else:
        print("Acesso negado")
    
