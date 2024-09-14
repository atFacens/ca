'''
Escreva um programa que leia duas notas de um aluno(a), calcule a média e informe se ele foi 
aprovado ou não. Considere que a média para aprovação é 7.0
Para ser aprovado, também precisa ter menos de 10 faltas
'''

# 1. entrada
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
faltas = int(input('Informe o número de faltas: '))

# 2. processamento
media = (nota1 + nota2) / 2
aprovado = (media >= 7) and (faltas < 10)

# 3. saída
print('Sua média é', media)
print('Você teve', faltas, 'falta(s)')
print('Aluno aprovado?', aprovado)
print('Aluno reprovado?', not aprovado)
