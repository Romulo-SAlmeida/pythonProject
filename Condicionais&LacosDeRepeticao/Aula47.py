"""
Exercicios para digitar nome e trabalhar indices 
"""

print('-------------------------------------')
nome = input('  Digite o seu nome   ')
print('--------------------------------------')
idade = input('  Digite sua idade   ')
int_idade = int(idade)

if nome and idade:     #Apresenatndo somente essa condição de boolean e false se nada for digitado nesse campo ele cai em 'else'
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}') #Esse '{nome[::-1]}' faz a variavel ficar ao contrario
    
    if ' ' in nome:       #Apresenta a condição que se o nome tiver espaço
        print('Seu nome contém espaço')
    else:
        print('Seu nome não contém espaço')

    print(f'Ele contém {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')   #Demonstra o primeiro indice
    print(f'A ultima letra do seu nome é {nome[-1]}')    #Demonstra o ultimo indice

elif int_idade  <= 0:
    print('Valores de idade não correspondente') 
else:
    print('Campo vazio')



    





