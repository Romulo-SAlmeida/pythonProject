""" Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
    C = 5 * ((F-32) / 9)."""

temperaturaf = float(input("Digite a temperatura em graus Fahrenheit, para que possa ser tranformada em Celsius: "))
temperaturac = 5*((temperaturaf-32)/9)
print(f'Sua temperatura é {temperaturac} C')
