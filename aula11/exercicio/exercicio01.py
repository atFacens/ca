# Escreva um programa que leia 4 valores digitados pelo usuário, e apresente a soma destes valores


soma = 0
contador = 1 

while contador < 5: 
    mensagem = 'Digite o ' + str(contador) + 'º número: '; 
    numero = int(input(mensagem))
    
    soma = soma + numero # soma é um acumulador

    contador = contador + 1 

print('A soma dos números é:', soma)