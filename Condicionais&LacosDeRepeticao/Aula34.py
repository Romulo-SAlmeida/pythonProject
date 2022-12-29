"""
Ultilizando condicionais 
"""
entrada = input('Você deseja sair do sistema?')

if entrada == 'sim':                          #Após construir a condicional e ir para próxima linha sempre dar TAB 
    print('Saida com sucesso')
elif entrada == 'não':
    print('Ok, continuar no sistema')
else:
    print('Erro')

