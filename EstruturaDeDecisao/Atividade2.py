"""Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo."""
numero= int(input("Digite qualquer valor: "))
if numero > 0:
    print("Seu número é positivo")
elif numero < 0:
    print("Seu número é negativo")
else:
    print("Seu número é neutro")