'''
Escrever um programa que indique se uma pessoa pode ou não dirigir.

'''

# 1. Entrada de dados

# 2. Processamento: 
# verificar se os dados de entrada correspondem a uma condição verdadeira ou falsa

# 3. Exibir a resposta

idade = int(input('Digite a sua idade: '))
temHabilitacao = input('Você tem habilitação (s/n)? ')

podeDirigir = (idade >= 18) and (temHabilitacao == 's')

print('Pode dirigir? ', podeDirigir)
