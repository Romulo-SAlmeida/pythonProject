"""
Formatando Strings com 'Format'
"""
a = 'b'
b = 5        
c = 's'

apresentacao = 'escolha={0} valor={2} escolha certa={1}'
formato = apresentacao.format(a,b,c)

print(formato)