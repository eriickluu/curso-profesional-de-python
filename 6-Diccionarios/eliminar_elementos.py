# VIDEO - Eliminar elementos

# -

diccionario = { 'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8 }

print(len(diccionario))
print(diccionario)

# Eliminar llave y valor de un diccionario
# del diccionario["a"]
# print(diccionario)

# Eliminar pero retornando el valor que se elimina
valor = diccionario.pop("b")
print(valor)

# Vaciar diccionario
diccionario = {}
print(diccionario)

# Limpiar diccionario
diccionario.clear()
print(diccionario)

