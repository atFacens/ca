
cont = 0

while cont < 10:
    cont += 1

    if cont == 5:
        continue # volta para o inicio do laço
    
    print(cont)

    if cont == 7:
        break # interrompe a execução do laço

print('fim')