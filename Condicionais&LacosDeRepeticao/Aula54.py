# Atividades

"""
1- Faça um programa que peça ao usuario para digitar um número inteiro, informe
se este número é para ou impar. Caso o usuario não digite um número inteiro, 
informa que não é um número inteiro

"""
from operator import contains


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
print('---------------------------------------------')
Hora = input('Digite somentes as horas    ')
Hora_inteira = int(Hora)

if Hora_inteira >= 0 and Hora_inteira <= 11:
    print('Bom dia')
elif Hora_inteira >= 12 and Hora_inteira <= 17:
    print('Boa tarde')
elif Hora_inteira >= 18 and Hora_inteira <= 23:
    print('Boa noite')
else:
    print('Digite um valor valido') 

print('---------------------------------------------')
""" 

3- Faça um programa que peça o primeiro nome do usuário. 
Se o nome tiver 4 letras ou menos, escreva "Seu nome é curto", 
se tiver entre 5 e 6 letras, escreva "Seu nome é normal",
se o nome tiver mais que 6 letras, escreva "Seu nome é muito grande"

"""
Nome = input('Digite seu primeiro nome   ')

if len(Nome) <= 4:
    print('Seu nome é curto')
elif len(Nome) >= 5 and len(Nome) <= 6:
    print('Seu nome é normal ')
else:
    print('Seu nome é muito grande')



