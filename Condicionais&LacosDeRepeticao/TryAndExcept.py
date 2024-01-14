'''Criando exceções com 'try' e 'except' '''

"""
Try = tenta executar o codigo
except = ocorreu algum erro ao tentar executar

"""

numero_str = input('Digite sua senha  ')

try:
    numero_int = int(numero_str)
    numero_senha = 123456
    if numero_int == numero_senha:
        print('Acesso permitido')
    else:
        print('Acesso negado')
except:
    print('Apenas números')