
def contabilizar(qtdePessoas : int):
    if(qtdePessoas < 51):
        cores.append('Azul') 
    elif(qtdePessoas < 101):
         cores.append('Amarelo')
    elif(qtdePessoas < 151):
        cores.append('Laraja')
    else:
        cores.append('Vermelho')


# entrada
    # --> obter o número de pessoas por vagão - ok
    # --> verificar se o número é válido - exercício 1

composicao = []
cores = []
total = 0

# Resposta - exercício 1
# no caso de não permitir o avanço para a próxima iteração, o mais 
# usual é while, no lugar do for

carro = 0
while(carro < 5):
    pessoas = int(input('Digite o número de pessoas no carro '+ str(carro+1) +': '))
    if(pessoas >= 0 and pessoas <= 250):
        composicao.append(pessoas)
        carro += 1
    else:
        print("O número de pessoas deve ser entre 0 e 250")


# processamento

# --> para cada carro:
    # --> comparar o número de pessoas com as cores - ok
    # --> somar o total de pessoas - ok

    # -- exercício 2: transformar esse bloco if/else em uma função

for carro in range(5):
    total += composicao[carro]
    contabilizar(composicao[carro])


# saída 

# --> pessoas e cores por vagão - ok
# --> total de pessoas na composição - ok

print('Total de pessoas: ' + str(total))
for carro in range(5):
    print('carro: ' + str(carro+ 1)  + '# pessoas: '+ str(composicao[carro]) +' cor: ' + cores[carro])
