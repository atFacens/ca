# lista: dinâmica, é possível alterar os elementos e a quantidade de elementos

lista1 = [5, 2, 7, 2, 9, 12, 15]

print(type(lista1)) # mostra o tipo da lista

print(dir(lista1)) # quais são as funções e dados da lista

print(len(lista1))  # exibe o tamanho da lista
lista1.append(20) # adiciona um novo elemento na lista
print(len(lista1))
lista1.remove(2) # remove um elemento da lista
print(len(lista1))

print(lista1) # exibe a lista



