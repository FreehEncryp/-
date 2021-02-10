#CALCULADORA EM PYTHON BÁSICA
from time import sleep
var1 = 0
var2 = 0
def linha():
    print('===' * 11)
op1 = str(input('Deseja acessar a Calculadora1 ou a Calculadora2? (C1/C2): '))
if op1 == 'C1' or op1 == 'c1':
    linha()
    var1 = int(input('Digite um número: '))
    operador = str(input('Digite o operador: '))
    var2 = int(input('Digite mais um número: '))
    soma = var1 + var2
    subtração = var1 - var2
    multiplicação = var1 * var2
    divisão = var1 / var2
    linha()
    if operador == '+':
        print(f'Resultado: {soma}')
    if operador == '-':
        print(f'Resultado: {subtração}')
    if operador == '*':
        print(f'Resultado: {multiplicação}')
    if operador == '/':
        print(f'Resultado: {divisão}')
    if var1 == '0' and var2 == '0' and operador == '/':
        var1 = 0
        operador = '/'
        print('Não é possível dividir por zero.')
if op1 == 'C2' or op1 == 'c2':
    linha()
    var1 = int(input('Digite um número: '))
    var2 = int(input('Digite mais um: '))
    soma = var1 + var2
    subtração = var1 - var2
    multiplicação = var1 * var2
    divisão = var1 / var2
    sleep(0.5)
    linha()
    print(f'Resultados:\nSoma: {soma}\nSubtração: {subtração}\nMultiplicação: {multiplicação}\nDivisão: {divisão}')
