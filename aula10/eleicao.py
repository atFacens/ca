totalEleitores = int(input('Quantos eleitores teremos?'))

candidato1 = 0
candidato2 = 0
candidato3 = 0
brancos = 0
nulos = 0

cont = 1
while cont <= totalEleitores:
    print('Eleitor', cont, 'de', totalEleitores)
    voto = input('Digite o seu voto: ')
    print('Você votou:', voto)

    # if voto == '1':
    #     candidato1 += 1
    # elif voto == '2':
    #     candidato2 += 1
    # elif voto == '3':
    #     candidato3 += 1
    # elif voto == '4':
    #     brancos += 1
    # else:
    #     nulos += 1      

    match voto:
        case '1':
            candidato1 += 1
        case '2':
            candidato2 += 1
        case '3':
            candidato3 += 1
        case '4':
            brancos += 1
        case _:
            nulos += 1

    cont += 1 # cont = cont + 1

# Exibir o vencedor
if candidato1 > candidato2 and candidato1 > candidato3:
    print('Candidato 1 venceu!')
elif candidato2 > candidato1 and candidato2 > candidato3:
    print('Candidato 2 venceu!')
elif candidato3 > candidato1 and candidato3 > candidato2:
    print('Candidato 3 venceu!')
elif candidato1 == candidato2 and candidato1 == candidato3:
    print('Todos os Candidatos empataram!')
elif candidato1 == candidato2:
    print('Candidatos 1  e 2 empataram!')
elif candidato1 == candidato3:
    print('Candidatos 1  e 3 empataram!')
else:
    print('Candidatos 2  e 3 empataram!')

# votos_validos = candidato1 + candidato2 + candidato3
votos_validos = totalEleitores - brancos - nulos

# Exibir as estatísticas
print('Candidato 1', candidato1, (candidato1 / votos_validos) * 100, '%')
print('Candidato 2', candidato2, (candidato2 / votos_validos) * 100, '%')
print('Candidato 3', candidato3, (candidato3 / votos_validos) * 100, '%')
print('Bracos', brancos, (brancos / totalEleitores) * 100)
print('Nulos', nulos, (nulos / totalEleitores) * 100)