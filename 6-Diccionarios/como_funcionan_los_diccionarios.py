# VIDEO - Cómo funcionan los diccionarios

# -Si la llave no existe dentro del diccionario se almacena el valor y se agrega al diccionario
# -Si se repite alguna llave almacena el ultimo valor el cual se le fue asignado

# Diccionario vacío
diccionario = {}

# Agregar una llave con su valor
diccionario['nombre'] = ' erick'

print(diccionario)

# Obtener un valor
valor = diccionario['nombre']

# Modificar un valor
diccionario['nombre'] = 'Erick Modificado'

print(diccionario)
print(valor)

diccionario = { "a": 1, "b":2, "c":3, "a":4 }

print(diccionario)

