
print('1 - cadastrar')
print('2 - alterar')
print('3 - apagar')
print('4 - consultar')
print('5 - sair')

numero = input('Digite sua opção: ')

match numero:
    case '1':
        nome = input('Informe o nome para o cadastro: ')
        print(nome, ' cadastrado')
    case '2':
        nome = input('Informe o nome para alteração: ')
        print(nome, ' alterado')
    case '3':
        nome = input('Informe o nome para apagar: ')
        print(nome, ' apagado')
    case '4':
        nome = input('Informe o nome para pesquisar: ')
        print(nome)
    case '5':
        print('Fim')
    case _:
        print('opção invalida')
