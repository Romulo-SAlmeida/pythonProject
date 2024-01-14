"""
Trabalhando com operadores de comparação.
"""

maior = 2>1   #Coparação que especifica que 2 é maior que 1
menor = 0<1  #Coparação que especifica que 0 é menor que 1
igualOuMaior = 2>=1 #Comparação que especifica que 2 e igual ou maior que 1
igualOUMenor = 0<=1 #Comparação que especifica que 0 é igual ou menor que 1
igual = 2 == 2 #Comparação que diz ue o primeiro valor é igual o segundo
diferente = 2 != 1  #Comparação que especifica valores diferentes


entrada_Cpf = input('Digite seu CPF ')      #Comparação ultilizando 'and' para acrescentar mais uma opção no laço condicional
entrada_senha = input('Digite sua senha ')               
if entrada_senha == '123456789' and entrada_Cpf == '70713877103':
    input('Acesso permitido')
else:
    input('Acesso negado')



busca_placa = input('Nome do dispositivo:')            #Ultilize o 'or' para criar um 'ou'
placa = 'XVCMMega'                         
if busca_placa == placa or busca_placa == 'xvcmmega':
    print("Encontrado")
else:
    print('Não encontrado')





