lista = [1,2,3,4]

print(sum(lista))

soma = 0
# for i in range(0, 4): # para cada posição (0...3)
for i in range(len(lista)): # para cada posição (0...3)
    soma = soma + lista[i]
print('soma = ', soma)

soma = 0
for num in lista: # para cada número da lista
    soma = soma + num
print('soma = ', soma)

