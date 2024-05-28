#lista
cidades = ['Brasília','Paranoá','Taguatinga','Gama','Sobradinho']

#informa a posição do item a ser deletado
indice = int(input('Informe a posição do item a ser deletado:  '))

#evita que o usuário apague o último item da lista caso indice=0
if indice > 0:
    indice -= 1
else:
    indice = ''

#deleta item da lista
try:
    del(cidades[indice])
    #exibe a lista
    for cidade in cidades:
        print(cidade)

except:
    print('Não foi possivel deletar este item, tente novamente.')

