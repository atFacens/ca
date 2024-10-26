populacaoInicial = int(input('População inicial: '))
taxaCrescimento = float(input('Taxa de crescimento mensal: '))
tempo = int(input('Número de meses: '))

populacaoFinal = populacaoInicial
for mes in range(tempo):
    populacaoFinal += int(populacaoFinal * taxaCrescimento)

print('Total final: ' + str(populacaoFinal))