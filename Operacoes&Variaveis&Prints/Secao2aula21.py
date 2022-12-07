"""
Utilizando 'Input' para salvar dados em uma variavel
"""
valorA = int(input('Digite o primeiro valor '))
valorB = int(input("Digite o segundo valor "))

valorC = valorB+valorA

print(f"O valor é {valorC}")

"""
Exercicios
"""

A = float(input('Digite o primeiro valor '))
B = float(input('Digite o segundo valor '))

c = A
A = B
B = c

print(f'O Valor foi trocado e A vale {A} e B vale {B}')