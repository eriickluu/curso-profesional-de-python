# VIDEO - Ciclo for

# -Los objetos iterables son las listas, tuplas, string y diccionarios
# -Cuando iteras un diccionario obtienes las llaves

numeros = [1,2,3,4,5,6,7,8,9,10]

diccionario = {'a': 1, 'b': 2}

valores = ((10,20),["strigs", "strings"],(True, False))

for numero in numeros:
    print(numero)

for valor, valor2 in valores:
    print(valor, valor2)

for llave in diccionario:
    print(llave)