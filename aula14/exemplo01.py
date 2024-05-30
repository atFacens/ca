
m = [ [1, 2, 3], 
     [4, 5, 6],
     [7, 8, 9] ]

# for linha in range(3):
#     for coluna in range(3):
#         print(linha, coluna, m[linha][coluna])

for linha in range(3):
    for coluna in range(3):
        print(m[linha][coluna], end=", ")
    print() # pula para próxima linha