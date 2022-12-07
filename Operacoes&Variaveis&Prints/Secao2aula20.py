"""
Formatação de Strings
"""
nome = 'luiz'
idade = 32
altura = 1.90
e_maior = idade > 18
peso = 80
imc = peso/ (altura*2)

print(nome, ' tem a idade de ',idade,' ,possui a altura de '
      ,altura ,' ,sua maioridade è ', e_maior, ' e seu imc é ', imc)

print(f' O {nome} tem {idade} anos de idade, possui {altura:.2f} de altura e imc de {imc:.2f}' )
