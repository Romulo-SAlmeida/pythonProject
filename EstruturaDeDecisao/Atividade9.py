"""Faça um Programa que leia três números e mostre-os em ordem decrescente"""

valor1 = int(input("Digite o primeiro número: "))
valor2 = int(input("Digite o segundo número: "))
valor3 = int(input("Digite o terceiro número: "))

if valor1 > valor2 and valor2 > valor3:
    print(f'{valor1}, {valor2} e {valor3}')
elif valor2 > valor3 and valor3 > valor1:
    print(f'{valor2}, {valor3} e {valor1}')
elif valor3 > valor1 and valor1 > valor2:
    print(f'{valor3}, {valor1} e {valor2}')
elif valor1 > valor3 and valor3 > valor2:
    print(f'{valor1}, {valor3} e {valor2}')
elif valor3 > valor2 and valor2 > valor1:
    print(f'{valor3}, {valor2} e {valor1}')
elif valor2 > valor1 and valor1 > valor3:
    print(f'{valor2}, {valor1} e {valor3}')
else:
    print('Não é permitido letras e números iguais')


