# VIDEO - Comprimir y Descomprimir tuplas

# -

tupla = (1, 2, 3, 4, 5, 6)
# uno, dos, tres, cuatro = tupla[0], tupla[1], tupla[2], tupla[3]
uno, dos, tres, *cuatro = tupla

print(uno)
print(dos)
print(tres)
print(cuatro)

lista = [10, 20, 30, 40]

# Regresa un objeto tipo zip
resultado = zip(tupla, lista)
resultado = tuple(resultado)
print(resultado)

resultado = zip(tupla, lista)
resultado = list(resultado)
print(resultado)

tupla_dos = (100, 200, 300, 400)

resultado = zip(tupla, lista, tupla_dos)
resultado = list(resultado)
print(resultado)
