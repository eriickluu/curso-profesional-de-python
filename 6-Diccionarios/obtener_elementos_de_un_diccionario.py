# VIDEO - Obtener elementos de un diccionario

# -

diccionario = { "a": 1, "b":2, "c":3, "a":4 }

resultado = diccionario["a"]

print(resultado)

# Ocurre error si buscamos una llave que no existe
# resultado = diccionario["z"]

# print(resultado)

resultado = "z" in diccionario

print(resultado)

# Retornar el valor de una llave que si existe y si no existe retorna None
resultado = diccionario.get("a")

# Retornar valor cuando la llave no existe
# Esta es la mas recomendable
resultado = diccionario.get("z", "La llave no existe") 

print(resultado)

# Generar una nueva llave/valor al diccionario en caso de que no exista y retornaría su valor
resultado = diccionario.setdefault("z", {}) 

print(resultado)