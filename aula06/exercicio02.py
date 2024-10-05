# Leia as duas notas e o número de faltas de aluno e informe se ele 
# foi aprovado ou não.
# Para ser aprovado o aluno deve ter no máximo 10 faltas e ter média
# pelo menos 7.0

# Se o aluno não foi aprovado,mas teve média pelo menos 5, ele ficou de exame

# entrada
# > nome, nota 1 e nota 2, faltas
nome = input('Digite o nome do aluno: ')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
faltas = int(input('Digite o número de faltas: '))

# processamento
# > calcular a média
media = (nota1 + nota2) / 2

# > verificar as faltas (no máximo 10 para aprovado)
# > verificar se a média é >= 7
# if( (faltas <= 10) and (media >= 7) ):

aprovadoPorFaltas = faltas <= 10 # True ou False
aprovadoPorNota = media >= 7
estaDeExame = media >= 5

if aprovadoPorFaltas:
    if aprovadoPorNota:
        resultado = "Auno Aprovado"
    else:
        if estaDeExame:
            resultado = "Aluno em exame"
        else:
            resultado = "Aluno reprovado"
else:
    resultado = "Reprovado por faltas"

# saída
# > nome , média, faltas, aprovado/reprovado

print(nome)
print('Média:', media, ' Faltas:', faltas)
print('Resultado:', resultado)