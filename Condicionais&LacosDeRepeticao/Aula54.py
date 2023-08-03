# Atividades

"""
1- Faça um programa que peça ao usuario para digitar um número inteiro, informe
se este número é para ou impar. Caso o usuario não digite um número inteiro, 
informa que não é um número inteiro

"""
Numero= input('Digite algum valor inteiro   ')

try:
    
    Numero_inteiro = float(Numero)
    if Numero_inteiro % 2 == 0:
        print('Esse número é par')
    else:
        print('Esse número é impar')
except:
    print('Digite um número inteiro')


"""
2-Faça um programa que pergunte a hora ao usuario e baseando-se no horario descrito, exiba a 
saudação apropriada. Ex.:
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23

"""

""" 
3- Faça um programa que peça o primeiro nome do usuário. 
Se o nome tiver 4 letras ou menos, escreva "Seu nome é curto", 
se tiver entre 5 e 6 letras, escreva "Seu nome é normal",
se o nome tiver mais que 6 letras, escreva "Seu nome é muito grande"

"""