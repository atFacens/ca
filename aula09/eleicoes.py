candidato1 = 0
candidato2 = 0
candidato3 = 0
candidato4 = 0
brancos = 0
nulos = 0

totalEleitores = 50

cont = 1
for cont in range (0, totalEleitores):
    print('1 à 4 número do seu candidato.')
    print('5 para nulo e 6 para branco.')
    voto = input('Digite o seu voto: ')

    if(voto == '1'):
        candidato1 += 1
    elif(voto == '2'):
        candidato2 += 1
    elif(voto == '3'):
        candidato3 += 1
    elif(voto == '4'):
        candidato4 += 1
    elif(voto == '5'):
        nulos += 1
    elif(voto == '6'):
        brancos += 1
    else:
        nulos += 1
    
    # match, case '1', case '2'

votosValidos = totalEleitores - brancos - nulos
print('Candidato 1:', candidato1, ':', (candidato1 / votosValidos) * 100, '%')
print('Candidato 2:', candidato2, ':', (candidato2 / votosValidos) * 100, '%')
print('Candidato 3:', candidato3, ':', (candidato3 / votosValidos) * 100, '%')
print('Candidato 4:', candidato4, ':', (candidato4 / votosValidos) * 100, '%')
print('Brancos:', brancos, ':', (brancos / totalEleitores) * 100, '%')
print('Nulos:', nulos, ':', (nulos / totalEleitores) * 100, '%')