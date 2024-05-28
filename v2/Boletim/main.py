#entrada
nome = input('Nome do Aluno: ')
nota = str(input('Informe sua nota: ')).replace(',','.')

#converte a nota para float
nota = float(nota)

#verifica nota
if nota >= 7:
    print(f'Parabéns {nome}, você está aprovado.')
elif nota >= 5:  #é como se fosse um meio termo, posso usar vários.
    print(f'{nome}, você está de recuperação.')
else:
    print(f'{nome} você está reprovado.')