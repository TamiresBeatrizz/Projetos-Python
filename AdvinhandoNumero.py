import random

# Palpite do computador
def gera():
    return random.randint(1,100) 


# Função que começa
def game():
    resposta = int(gera())
    tentativa = 0 # conta a tentativa do jogador (usuário)
    print("\nPalpite gerado!")


    # Chute do usuário
    chute =0
    while chute is not resposta:
        tentativa = +1
        chute = int(input('Qual o seu chute?  '))
        if chute > resposta:
            print('Errou, é um valor menos que ', chute)
        elif chute < resposta:
            print('Errou, é valor maior que ', chute)
        else:
            print("Parabéns! O número gerado foi ",resposta, 
                  "Acertou em ",tentativa," tentativas!")


while True:
    game()
