# JOGO: PAPEL, PEDRA E TESOURA

from os import system, name 
import random
system('cls')

print('Escolha uma opção para jogar: ')

opcao = 's'
while opcao.upper()=='S':
    system('cls') if (name == 'nt') else system('clear')

    computador = random.randint(0,2)
    jogador = int(input(''' Escolha uma opção para se jogar:
                    [0] Pedra
                    [1] Papel
                    [2] Tesoura
                    Digite sua escolha:  '''))

    pecas= ('Pedra', 'Papel', 'Tesoura')

# Imprimir jogadas
    print('Você escolheu {}' .format(pecas[jogador]))
    print('O computador escoheu {}' .format(pecas[computador]))

# Tabela - tupla muiltidimensional
# Informações da partida:
    tabela = ((0,1,-1), (-1,0,1), (1,-1,0))

    jogada = tabela[computador] [jogador]

# verificação de jogada 
    if jogada == 0:
        resultado = 'Deu empate vocês escolheram a mesma peça'
    elif jogada == 1:
        resultado = 'Você ganhou!'
    else:
        resultado = 'O computador ganhou'

# tela resultado // Desejo de continuar     
    print(resultado)
    opcao = input('jogar novmanete? Aperte S(sim) para jogar novamente.')
else:
    print('Você escolheu sair.')
    print('Obrigado pelo o jogo! \nVolte sempre :)')
