entrada = input('Digite um número com 3 dígitos:')
numero = int(entrada)

digito3 = numero % 10 # separa o ultimo digito do número

numero = numero // 10 # descarta o último dígito do número (divisão inteira)

digito2 = numero % 10

digito1 = numero // 10

print(digito1, digito2, digito3)