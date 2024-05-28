#tratamento de erro
try:
    #entrada de dados
    n1 = str(input('Informe o primeiro número:')).replace(',','.')
    n2 = str(input('segundo número:')).replace(',','.')

    n1 = float(n1)
    n2 = float(n2)

    soma = (n1+n2)

    print(f'{soma}')

#caso o programa dê erro, irá continuar o código exibindo a mensagem a seguir:
except:         
    print('Caracter inválido!')