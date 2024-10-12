# Escreva um programa que leia 4 valores digitados pelo usuário, 
# e apresente a soma destes valores

cont = 1
soma = 0
print('Digite 4 valores inteiros:')
while(cont < 5):
    valor = int(input('Digite o ' + str(cont) + 'º valor:'))
    soma = soma + valor # soma += valor
    cont += 1 # cont = cont + 1

print('soma = ' + str(soma))