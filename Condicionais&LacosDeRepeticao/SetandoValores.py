"""
Ultilizando 'input' para coletar dados de usuário
"""
numero1 = input('Digite o primeiro valor: ')     #Com o 'input' eu salvo os valores que o usuario digitou em format string
numero2 = input('Digite o segundo valor: ')

print(f'A soma desses valores é {numero1 + numero2}')


# Agora vamos transformar essa String em numeros inteiros

numero1 = input('Digite o primiero valor: ')
numero2 = input('Digite o segundo valor: ')

int_numero2 = int(numero2)
int_numero1 = int(numero1)

print(f'A soma dos valores é {int_numero1+int_numero2}')