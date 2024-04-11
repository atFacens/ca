# Aprovado = nota >= 7 e também faltas < 12
# Faltas >= 12 reprovado
# Nota >= 5 Exame
# Nota < 5 Reprovado
# entrada de dados

nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
faltas = int(input('Quantas faltas? '))

# processamento
media = (nota1 + nota2) / 2

if faltas > 12:
    resposta = 'Reprovado por faltas'
else:
    if media >= 7:
        resposta = 'Aprovado'
    else:
        if media >= 5:
            resposta = 'Exame'
        else:
            resposta = 'Reprovado por nota'

# saída
print('O(A) auno(a) está ', resposta)