frase = input('Digite a frase: ')
cont = 0
lista = list(frase)

print(frase)
print(lista)

nova_frase = ''
# for letra in frase:
#     if(letra != 'a' and letra != 'e' and letra != 'i' and letra != 'o' and letra != 'u'):
#         # print(letra, end='')
#         nova_frase += letra
#     else:
#         cont += 1
for i in range(0, len(frase)):

    if(lista[i] == 'a' or lista[i] == 'e' or lista[i] == 'i' or lista[i] == 'o' or lista[i] == 'u'):
        # print(letra, end='')
        lista[i] = ' '
        cont += 1
    
print(lista)
nova_frase = ''.join(lista)
print(nova_frase)
print('\nvogais', cont)
