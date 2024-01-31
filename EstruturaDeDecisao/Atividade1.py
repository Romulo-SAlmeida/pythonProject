"""Faça um Programa que peça dois números e imprima o maior deles."""

primeiro_numero = int(input("Digite algum número para comparar: "))
segundo_numero = int(input("Digite outro número para comparar: "))

if primeiro_numero > segundo_numero:
    print(f"O primeiro número é maior: {primeiro_numero}")
elif primeiro_numero == segundo_numero:
    print("OS dois valores são iguais")
else:
    print(f"O segundo valor é maior: {segundo_numero}")