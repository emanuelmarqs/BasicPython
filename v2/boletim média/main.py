nome = input('Nome do aluno: ')
sexo = input('Qual o seu sexo? Digite M para masculino, e F para feminino.')
nota1 = str(input('Digite sua primeira nota: ')).replace(',','.')
nota2 = str(input('Digite sua segunda nota: ')).replace(',','.')
nota3 = str(input('Digite sua terceira nota: ')).replace(',','.')
nota4 = str(input('Digite sua quarta nota: ')).replace(',','.')

nota1 = float(nota1)
nota2 = float(nota2)
nota3 = float(nota3)
nota4 = float(nota4)

media = float

media = (nota1+nota2+nota3+nota4)/4
print(f'{nome} sua média é:{media}')

if media >= 7 and sexo == ('M'):
    print(f'Parabéns {nome}, você foi aprovado.')
else: sexo == ('M') and media < 7
print(f'Sinto muito {nome}, você está reprovado.')

if media < 7 and sexo == ('F'):
    print(f'Parabéns {nome}, você foi aprovada.')
else: sexo == ('F') and media < 7
print(f'Sinto muito {nome}, você está reprovada.')



