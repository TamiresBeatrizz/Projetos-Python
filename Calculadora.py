# Criação de calculadora = Simples

def adicao(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y != 0:
        return x / y
    else:
        return 'divisão por zero não é permitida'

#...  definir outras operações  ...

while True:
    print('Escolha a operação.')
    print('0. Sair')
    print('1. Adição')
    print('2. Subtração')
    print('3. Multiplicação')
    print('4. Divisão \n')

    # ... outras opções ...

    escolha = input('Escolha(0-4): ')

    if escolha == '0':
        break

    num1 = int(input('Primeiro número:  '))
    num2 = int(input('Segundo número: '))

    if escolha == '1':
        print(num1, '+', num2, '=', adicao(num1, num2))
    elif escolha == '2':
        print(num1, '-', num2, '=', subtracao(num1,num2))
    elif escolha == '3':
        print(num1,'*', num2, '=', multiplicacao(num1, num2))
    elif escolha == '4':
        print(num1, '/', num2, '=', divisao(num1, num2))
    else:
        print('Entrada inválida \n')
    
    break