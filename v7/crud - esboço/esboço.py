



#lista
nomes = ['Alex', 'Simone', 'Natalia', 'Emanuel', 'Alexandra','Alice','Bedian','Caique','Dylan','Yago','Zurich']

# ordenando a lista em ordem alfabética
nomes.sort()

#nomes.sort(reverse = True) #ordena em ordem alfabetica inversamente

# for nome in nomes:  for simples
#     print(nome)

for i in range(len(nomes)):    #range é o tamanho da lista, saber quantas posições ela tem.
                           #len é uma função que tenta medir o tamanho da lista, enumera.
    print(f' {i + 1}° nome da lista: {nomes[i]}.')

nomes = ['Emanuel', 'Fernanda', 'Carlos', 'Carlota', 'Natalia', 'Emanuel']

#usuário informa o índice que deseja alterar
indice = int(input('Informe o índice que deseja alterar algum entre 1-6: '))
indice -= 1

# usuário informa o novo nome
nomes[indice] = input('Informe o novo nome:  ')

#exibe a lista
for nome in nomes:
    print(nome)



#lista vazia
tarefas = []

#laço de repetição - para quando não sei quantos itens terão a lista.
while True:
    #usuário informa os itens da lista de tarefas
    nova_tarefa = input('Informe a nova tarefa ou deixe vazio para encerrar e exibir a lista: ')

    #verifica se o usuário inseriu uma nova tarefa
    if nova_tarefa != '':  #se a tarefa for diferente de vazio ele continua o loop
        tarefas.append(nova_tarefa) #adiciona a nova tarefa à lista
        continue
    else:     #se não
        break #o loop será finalizado

#exibe a lista de tarefas
for tarefa in tarefas:
    print(tarefa)

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



#lista de frutas
frutas = ["Maracujá", "Banana", "Maça"]

#usuário informa o nome da nova fruta
nova_fruta = input('Informe o nome da fruta que deseja.')

#nova fruta é inserida na lista / append = acrescentar
frutas.append(nova_fruta)

#exibe na tela a nova lista
for fruta in frutas:
    print (fruta)