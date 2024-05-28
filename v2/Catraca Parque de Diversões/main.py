# Entrada
nome = input('Qual o seu nome? ')
idade = int(input('Qual a sua idade?'))
altura = str(input('Qual a sua altura?')).replace(',','.')

#converte altura para float
altura = float(altura)

#estrutura de decisão
if idade >= 12 and altura >= 1.20:
    print(f'Olá {nome}, divirta-se!')
else:
    print(f'Sinto muito {nome}, você não está autorizado.')




