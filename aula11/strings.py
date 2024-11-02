# slicing

# texto = "palavra"

# print(texto[2:4])
# print(texto[2:])
# print(texto[:4])


# formatação de string

# resultado = 5555.1299
# print("Resultado = " + str(resultado))

# # print("Resultado = {resultado}")
# print(f"Resultado = {resultado:.2f}")

# texto = "Texto sem Formato nOrmalizado"

# novo_texto = texto.lower()
# novo_texto = texto.upper()
# novo_texto = texto.capitalize()
# novo_texto = texto.title()

# print(novo_texto)
# print(texto)

# texto = "boa noite! Como vai sua noite?"

# print(texto.count("noite"))
# print(texto.find("noite"))
# print(texto.find("noite", 5))

# print(texto.startswith("boa"))
# print(texto.startswith("noite"))
# print(texto.endswith("noite?"))

# numero = "A"
# if(numero.isnumeric()):
#     print(int(numero) + 2)
# else:
#     print("Isso não é um número")

# texto = "asd123"
# print(texto.isalnum())
# print(texto.isalpha())
# print(texto.isnumeric())

texto = "123"
print(texto.isnumeric())
print(texto.isdigit())
print(texto.isdecimal())
