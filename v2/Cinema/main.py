#recebe o nome do usuário
nome = input('Informe o seu nome: ')

#exibe a lista de filmes e suas salas
print('LISTA DE FILMES \n')
print('Sala 1 - A volta dos que não foram.')
print('Sala 2 - A roda quadrada.')
print('Sala 3 - Poeira em alto mar.')
print('Sala 4 - As tranças do rei careca.')
print('Sala 5 - A vingança do peixe frito\n')

#recebe a sala esc olhida
sala = int(input('Informe a sala desejada: '))

match sala:   #mesma função do switch
    case 1:
        print(f'Filme escolhido por {nome}, A volta dos que não foram. \n')
    case 2:
        print(f'Filme escolhido por {nome}, A roda quadrada.\n')
    case 3: 
        print(f'Filme escolhido por {nome}, Poeira em alto mar.\n')
    case 4:
        print(f'Filme escolhido por {nome}, As tranças do rei careca.\n')
    case 5:
        print(f'Filme escolhido por {nome}, A vingança do peixe frito.\n')

    case _: 
        print('Sala inexistente!')