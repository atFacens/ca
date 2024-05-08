# entrada de dados

nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))

# processamento
media = (nota1 + nota2) / 2

if media >= 7:
    resposta = 'Aprovado'
elif media >= 5:
    resposta = 'Exame'
else:
    resposta = 'Reprovado'

# saída
print('O(A) auno(a) está ', resposta)
