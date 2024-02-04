"""Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido"""

sexo = input("Escolha a sua sexualidade digitando F - Feminino ou M - Masculino: ")

if sexo == "F":
    print("Sexo é feminino")
elif sexo == 'M':
    print("Sexo é masculino")
else:
    print("Digite novamente")