entrada = input("digite um número inteiro: ")
numero = int(entrada)

resto = numero % 2

e_par = resto == 0

if e_par:
    print(numero, "é par")
else:
    print(numero, "é impar")