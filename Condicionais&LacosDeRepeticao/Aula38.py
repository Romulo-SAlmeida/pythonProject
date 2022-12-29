"""
Peça para o usuario digitar um valor e mostre qual e maior e qual é menor
"""
valor1 = input('Digite o primeiro valor ')
valor2 = input('Digite o segundo valor ')

int_valor1 = int(valor1)
int_valor2 = int(valor2)

if valor1 > valor2:
    input(f'O valor {valor1} é maior que {valor2}')
elif valor1 < valor2:
    input(f'O valor {valor2} é maior que {valor1}')
else:
    input(f'Os valores são iguais {valor1} , {valor2}')

