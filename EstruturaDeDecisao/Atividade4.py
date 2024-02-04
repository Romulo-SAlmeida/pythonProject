"""Faça um Programa que verifique se uma letra digitada é vogal ou consoante."""

letra = input("Digite a letra aqui: ")

vogais = ['a','e','i','o','u']

if letra in vogais:
    print("Essa letra é uma vogal")
else:
    print("Essa letra é uma consoante")