# declaração de variáveis

nome = 'Emanuel' # string
idade = 18 # int
altura = 1.72 #ponto flutuante (float)
programador = True # lógica (booleana)

#saída de dados - 4 FORMAS

#1° FORMA
print('Nome:  ' + nome + '.' )
print('Idade:  ' +str(idade) + '.') #Concatenação APENAS PARA STRING!

#2° FORMA
print('Nome:  ', nome, '.') # Usar apenas a virgula - AGORA ELE IRÁ SERVIR PARA NÚMERICOS TAMBÉM
print('Idade:  ', idade, '.')

#3° FORMA
print('Nome: {}.' .format(nome))
print('Idade: {}.' .format(nome))
print('Meu nome é {} e tenho {} anos.' .format(nome, idade))

#4° FORMA - f-string .

print(f"Nome: {nome}.")
print(f"Idade: {idade}.")

#Verificar quais os tipos de variáveis foram utilizadas

print(type (nome))
print(type (idade))
print(type (altura))
print(type (programador))