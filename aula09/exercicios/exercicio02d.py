# entrada de dados

nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))

# processamento
media = (nota1 + nota2) / 2

# if media <= 5 and media < 7: alternativa para testar exame primeiro

if media < 7:
    if media >= 5:
        resposta = 'Exame'
    else:
        resposta = 'Reprovado'
else:
    resposta = 'Aprovado'
    

# saída
print('O(A) auno(a) está ', resposta)
