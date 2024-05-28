#Entrada de dados de usuário

nome = input('Informe o seu nome: ') #Recebe o nome do usuário
altura = str(input('Informe a seu altura: ')).replace(',','.') #replace vai converter a virgula em ponto.
#Após fazer isso, converto o tipo da variável .

#converte str para float
altura = float(altura)

#Saída de dados - EXIBE
print(f'Meu nome é {nome}.') #Exibe
print(f'Sua altura é: {altura}')