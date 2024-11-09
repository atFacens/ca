palavra = input('Digite a palavra: ')

numeroCaracteres = len(palavra)

cont = numeroCaracteres - 1
while cont > -1:
    print(palavra[cont], end="")
    cont -= 1

print('\n---')

for contar in range(numeroCaracteres-1, -1, -1):
    print(palavra[contar], end="")

# for 

# print(palavra[0])
# print(palavra[1])
# print(palavra[2])
# print(palavra[3])

# print(palavra[numeroCaracteres - 1])