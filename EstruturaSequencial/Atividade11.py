"""Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    o produto do dobro do primeiro com metade do segundo .
    a soma do triplo do primeiro com o terceiro.
    o terceiro elevado ao cubo."""

print('----------------------------------------------------------')
numero1 = int(input("\nDigite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))
numero_real= float(input("Digite um número real: "))

primeira= (numero1*2)*(numero2/2)
segunda= (numero1*3)+ numero_real
terceiro= numero_real*numero_real

print(f"O primeiro valor é {primeira}"
    f"\nO segundo valor é {segunda}"
      f"\nO terceiro valor é {terceiro}")
print('----------------------------------------------------------')