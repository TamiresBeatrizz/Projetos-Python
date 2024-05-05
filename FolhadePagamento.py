# FOLHA DE PAAGAMENTO 

from os import system , name
system('cls') if(name == 'nt') else system('clear')

print('**** FOLHA DE PAGAMENTO ****')
salario = float(input('Informe o seu salario: '))

# Calculo INSS
print(salario)
if salario > 7786.04:
    inss = 908.86
else:
    if salario > 4000.05:
       inssP = 0.14
       DeducaoInss = 181.18
    elif salario > 2666.70:
       inssP = 0.12
       DeducaoInss = 101.18
    elif salario > 1412.02:
       inssP = 0.09
       DeducaoInss = 21.18
    else:
       inssP = 0.075
       DeducaoInss = 0
    inss = (salario * inssP) - DeducaoInss

# Base salarial
base = salario - inss
print(base)

# Calcular IR
if base > 4664.68:
   salarioIR = 0.275
   deducao = 896.00
elif base > 3751.06:
   salarioIR = 0.225
   deducao = 662.77
elif base > 2826.66:
   salarioIR = 0.15
   deducao = 381.44
elif base > 2259.21:
  salarioIR = 0.075
  deducao = 169.44
else:
   salarioIR = 0
   deducao = 0

ir = (base * salarioIR) - deducao
SalarioLiquido = base - ir
print('Salário Bruto: {:.2f}\nSalário Base: {:.2f}\nINSS: {:.2f}\n%IR: {:.2f}%\nValor IR: {:.2f}\nSalário Liquido: {:.2f}' .format(salario, base, inss, salarioIR*100, ir, SalarioLiquido))