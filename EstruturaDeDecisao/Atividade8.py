"""Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
sabendo que a decisão é sempre pelo mais barato."""

produto1 = float(input("Insira o valor do primeiro produto: "))
produto2 = float(input("Insira o valor do segundo produto: "))
produto3 = float(input("Insira o valor do terceiro produto: "))

if produto1 < produto2 and produto1 < produto3:
    print(f'O primeiro produto é o com menor valor R$ {produto1}')
elif produto2 < produto1 and produto2 < produto3:
    print(f'O segundo produto é o com menor valor R$ {produto2}')
if produto3 < produto1 and produto3 < produto2:
    print(f'O terceiro produto é o com menor valor R$ {produto3}')