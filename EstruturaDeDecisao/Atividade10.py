"""Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso."""

turno = input('Digite qual a turno que você estuda, de acordo com a seguinte regra: ' 
              '\nM-matutino'
              '\nV-Vespertino' 
              '\nN- Noturno'
              '\nDe acordo com seu turno de estudo, digite a respectiva letra: ')
if turno == 'M':
    print('Bom Dia!')
elif turno == 'V':
    print('Boa tarde!')
elif turno == 'N':
    print('Boa noite!')
else:
    print('Valor inválido')