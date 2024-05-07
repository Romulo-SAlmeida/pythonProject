"""Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor
seja inválido e continue pedindo até que o usuário informe um valor válido."""


valor = int(input('Digite algum valor de 0 a 10: \n'))

while valor < 0 or valor > 10:
    print('Erro, Digite um valor aceitavel! \n')
    valor = input('Digite algum valor de 0 a 10 \n')