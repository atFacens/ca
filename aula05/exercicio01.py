# Escreva um programa que leia um valor numérico inteiro e informe 
# se o valor digitado é positivo ou negativo

numero = int (input('Digite um número inteiro: '))

ehPositivo = (numero >= 0)

if(ehPositivo):
    print('Este número é positivo')
else:
    print('Este número é negativo')