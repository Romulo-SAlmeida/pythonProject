""" As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para 
    desenvolver o programa que calculará os reajustes. Faça um programa que recebe o salário de um colaborador e o 
    reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento."""

salario_antigo= float(input('Digite aqui seu salario atual: '))

if salario_antigo <= 280:
    salario_novo =(salario_antigo*0.20) + salario_antigo
    print(f'O salário antes do reajuste: R$ {salario_antigo}'
            f'\nO percentual de aumento aplicado: 20%'
            f'\nO valor do aumento: {salario_antigo*0.20}'
            f'\nO novo salário: R${salario_novo}')
elif salario_antigo > 280 and salario_antigo <= 700:
    salario_novo = (salario_antigo*0.15) + salario_antigo
    print(f'O salário antes do reajuste: R$ {salario_antigo}'
            f'\nO percentual de aumento aplicado: 15%'
            f'\nO valor do aumento: {salario_antigo*0.15}'
            f'\nO novo salário: R${salario_novo}')
elif salario_antigo > 700 and salario_antigo <= 1500:
    salario_novo = (salario_antigo*0.10) + salario_antigo
    print(f'O salário antes do reajuste: R$ {salario_antigo}'
            f'\nO percentual de aumento aplicado: 10%'
            f'\nO valor do aumento: {salario_antigo*0.10}'
            f'\nO novo salário: R${salario_novo}')
else:
    salario_novo = (salario_antigo*0.05) + salario_antigo
    print(f'O salário antes do reajuste: R$ {salario_antigo}'
            f'\nO percentual de aumento aplicado: 5%'
            f'\nO valor do aumento: {salario_antigo*0.05}'
            f'\nO novo salário: R${salario_novo}')
    

