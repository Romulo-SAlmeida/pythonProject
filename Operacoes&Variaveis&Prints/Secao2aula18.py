"""
Trabalhando com variaveis e atividade com printagem na tela do usuario
"""
peso = 70.56
altura = 1.80
nome = 'José'
idade = 15
e_maiorDeIdade = idade>18
e_menorDeIdade = idade<18
imc = peso/(altura**2)
print('O paciente', nome, f', tem o imc de {imc:,.2f}')