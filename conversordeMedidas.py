# conversor de medidas 

from os import system 

system('cls')

print('**** CONVERSOR DE MEDIDAS ****')

medida = float(input('Informe a medida em centímetros: '))

print('\nEscolha para que unidade deseja converter')
print('1 - Polegada\n2 - Pé\n3 - Jarda')

menu = input('opção: ')

if menu == '1':
    Polegadas = medida / 2.54
    resultado = '{:.4f} centímetros correspondem a {:.4f} polegadas' .format(medida, Polegadas)
elif menu == '2':
    pes = medida /30.48
    resultado = '{:.4f} centímetros correspondem a {:.4f} jardas' .format(medida, pes)
elif menu == '3':
    jardas = medida / 91.44
    resultado = '{:.4f} centímetros correspondem a {:.4f} jardas' .format(medida, jardas)
else:
    resultado = 'você não escolheu uma das opções...'

print(resultado)