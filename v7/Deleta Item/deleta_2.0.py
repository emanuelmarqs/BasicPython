#lista
cidades = ['Brasília','Paranoá','Taguatinga','Gama','Sobradinho']

#usuário informa o nome que deseja deletar
cidade_deletada = input('Nome da cidade a ser deletada: ')

#deleta a cidade informada
try:
    cidades.remove(cidade_deletada)
    
#exibe a lista após a modificação
    for cidade in cidades:
        print(cidade)

except:
    print('Não foi possível deletar a cidade informada.')



