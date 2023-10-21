from random import randint
from time import sleep
print('Vamos jogar!')

itens = ('Pedra', 'Papel',  'Tesoura')

pc = randint(0, 3)

print('''Suas opções
[0] Pedra
[1] Papel
[2] Tesoura''')

print('👺' * 20)

player = int(input('Qual sua jogada? '))

print('JO')
sleep(1)

print('KEN')
sleep(1)

print('PO')
sleep(1)

if player in range(len(itens)):  

    print(f'O computador jogou:  {itens[pc]}')

    print(f'O player jogou: {itens[player]}')

print('👺' * 20)

if pc == 0:
    if player == 0:
        print('Empate')

    elif player == 1:
        print('Jogador venceu!')

    elif player == 2:
        print('Computador venceu!')
    else:
        print('Jogada invalida')

elif pc == 1:

    if player == 0:
        print('Computador venceu!')

    elif player == 1:
        print('Empate')

    elif player == 2:
        print('Jogador venceu!')

    else:
        print('Jogada invalida')

elif pc == 2:
    if player == 0:
        print('Jogador venceu!')

    elif player == 1:
        print('Computador ganha!')

    elif player == 2:
        print('Empate!')

    else:
        print('Jogada invalida')
