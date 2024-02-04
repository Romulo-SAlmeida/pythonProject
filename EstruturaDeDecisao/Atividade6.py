"""Faça um Programa que leia três números e mostre o maior deles."""

numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
numero3 = int(input('Digite o terceiro número: '))

if numero1 > numero2 or numero1 >numero3:
    print(f'O primeiro número é maior {numero1}')
elif numero2 > numero1 or numero2 >numero3:
    print(f'O segundo número é maior {numero2}')
elif numero3 > numero2 or numero3 > numero1:
    print(f'O terceiro número é maior {numero3}')