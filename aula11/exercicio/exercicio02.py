# escreva um programa que leia vários números digitados pelo usuário
# O programa deve perguntar no início, quantos números serão digitados
# Ao final, exiba a média dos valores digitados

soma = 0

quantidade = int(input('Quantos números serão digitados? '))

contador = 1 
while contador <= quantidade: 
    mensagem = 'Digite o ' + str(contador) + 'º número: '; 
    numero = int(input(mensagem))
    
    soma = soma + numero # soma é um acumulador

    contador = contador + 1 

print('A média dos números é:', soma / quantidade)